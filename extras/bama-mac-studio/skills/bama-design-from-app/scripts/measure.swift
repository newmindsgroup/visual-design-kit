#!/usr/bin/env swift
// Measures a screenshot so a design can be rebuilt from numbers, not guesses.
// Logical coordinates require a measured --scale. Use --pixels for pixel-only work.
//
//   swift measure.swift info   shot.png
//   swift measure.swift color  shot.png x y [x y ...]       hex color at each point
//   swift measure.swift hline  shot.png y [x0 x1]           color runs along a row
//   swift measure.swift vline  shot.png x [y0 y1]           color runs down a column
//   swift measure.swift rows   shot.png x0 x1 [y0 y1]       bands of content (text, icons) between x0 and x1
//   swift measure.swift cols   shot.png y0 y1 [x0 x1]       bands of content between y0 and y1
//   swift measure.swift palette shot.png [x y w h]          most used colors in a region
//   swift measure.swift ink    shot.png x y w h             text and icon colors: pixels far from the background
//   swift measure.swift crop   shot.png x y w h out.png [zoom]
// Options: --scale <verified factor> or --pixels (mutually exclusive)   --tolerance 12 (0-255, how different a color must be to count)

import AppKit
import CoreGraphics
import Foundation

var args = Array(CommandLine.arguments.dropFirst())
func option(_ name: String, _ fallback: Double) -> Double {
    guard let i = args.firstIndex(of: name) else { return fallback }
    guard i + 1 < args.count, let v = Double(args[i + 1]) else { print("invalid value for \(name)"); exit(2) }
    args.removeSubrange(i...(i + 1))
    return v
}
let declaredScale = args.contains("--scale")
let pixelOnly = args.contains("--pixels")
guard !(declaredScale && pixelOnly) else { print("choose --scale or --pixels, not both"); exit(2) }
if let index = args.firstIndex(of: "--pixels") { args.remove(at: index) }
let scale = option("--scale", 1)
let coordinateUnit = declaredScale ? "pt" : "px"
let tolerance = option("--tolerance", 12)
guard scale.isFinite, scale > 0, scale <= 8, tolerance.isFinite, (0...255).contains(tolerance) else {
    print("scale must be positive and at most 8; tolerance must be 0 to 255"); exit(2)
}

struct Bitmap {
    let width: Int, height: Int
    var data: [UInt8]

    init(path: String) {
        guard let source = CGImageSourceCreateWithURL(URL(fileURLWithPath: path) as CFURL, nil),
              let image = CGImageSourceCreateImageAtIndex(source, 0, nil) else {
            print("cannot read \(path)"); exit(1)
        }
        width = image.width; height = image.height
        guard width > 0, height > 0, width <= 16_384, height <= 16_384, width * height <= 40_000_000 else {
            print("image dimensions exceed the 40 megapixel safety limit"); exit(2)
        }
        data = [UInt8](repeating: 0, count: width * height * 4)
        let ctx = CGContext(data: &data, width: width, height: height, bitsPerComponent: 8, bytesPerRow: width * 4,
                            space: CGColorSpace(name: CGColorSpace.sRGB)!,
                            bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
        ctx.draw(image, in: CGRect(x: 0, y: 0, width: width, height: height))
    }

    func pixel(_ x: Int, _ y: Int) -> (Int, Int, Int) {
        let i = (min(max(y, 0), height - 1) * width + min(max(x, 0), width - 1)) * 4
        return (Int(data[i]), Int(data[i + 1]), Int(data[i + 2]))
    }
}

func hex(_ c: (Int, Int, Int)) -> String { String(format: "#%02X%02X%02X", c.0, c.1, c.2) }
func distance(_ a: (Int, Int, Int), _ b: (Int, Int, Int)) -> Double {
    Double(max(abs(a.0 - b.0), abs(a.1 - b.1), abs(a.2 - b.2)))
}
func px(_ points: String) -> Int { Int((Double(points) ?? 0) * scale) }
func pt(_ pixels: Int) -> String { String(format: "%g", Double(pixels) / scale) }

guard args.count >= 2 else {
    print("usage: swift measure.swift <info|color|hline|vline|rows|cols|palette|crop> shot.png ...")
    exit(1)
}
let command = args[0]
guard command == "info" || declaredScale || pixelOnly else {
    print("coordinates require --scale <verified factor> or --pixels; logical scale is unknown"); exit(2)
}
let bitmap = Bitmap(path: args[1])
let rest = Array(args.dropFirst(2))
let counts: [String: Set<Int>] = ["info": [0], "color": Set(stride(from: 2, through: 32, by: 2)), "hline": [1, 3], "vline": [1, 3], "rows": [2, 4], "cols": [2, 4], "palette": [0, 4], "ink": [4], "crop": [5, 6]]
guard let expected = counts[command], expected.contains(rest.count) else { print("invalid command or argument count"); exit(2) }
let numeric = command == "crop" ? Array(rest.prefix(4)) + Array(rest.dropFirst(5)) : rest
for value in numeric {
    guard let number = Double(value), number.isFinite, number >= 0, number <= 32_768 else { print("coordinates must be bounded nonnegative numbers"); exit(2) }
}
if command == "color" {
    for pair in stride(from: 0, to: rest.count, by: 2) {
        guard px(rest[pair]) < bitmap.width, px(rest[pair + 1]) < bitmap.height else { print("point outside image"); exit(2) }
    }
}
if command == "hline" || command == "vline" {
    let axisLimit = command == "hline" ? bitmap.height : bitmap.width
    let runLimit = command == "hline" ? bitmap.width : bitmap.height
    guard px(rest[0]) < axisLimit else { print("line outside image"); exit(2) }
    if rest.count == 3 { guard px(rest[1]) <= px(rest[2]), px(rest[2]) < runLimit else { print("invalid line range"); exit(2) } }
}
if command == "rows" || command == "cols" {
    let primaryLimit = command == "rows" ? bitmap.width : bitmap.height
    let secondaryLimit = command == "rows" ? bitmap.height : bitmap.width
    guard px(rest[0]) < px(rest[1]), px(rest[1]) <= primaryLimit else { print("invalid region"); exit(2) }
    if rest.count == 4 { guard px(rest[2]) < px(rest[3]), px(rest[3]) <= secondaryLimit else { print("invalid region"); exit(2) } }
}
if ["crop", "ink", "palette"].contains(command), rest.count >= 4 {
    guard px(rest[2]) > 0, px(rest[3]) > 0, px(rest[0]) + px(rest[2]) <= bitmap.width, px(rest[1]) + px(rest[3]) <= bitmap.height else { print("region outside image"); exit(2) }
}
if command == "crop" {
    guard !FileManager.default.fileExists(atPath: rest[4]) else { print("output already exists; choose a new path"); exit(2) }
    if rest.count == 6 { guard let zoom = Double(rest[5]), zoom > 0, zoom <= 8 else { print("zoom must be positive and at most 8"); exit(2) } }
}

/// Prints runs of similar color along a line of pixels.
func runs(_ samples: [(Int, (Int, Int, Int))]) {
    guard var start = samples.first else { return }
    var last = start
    for sample in samples.dropFirst() {
        if distance(sample.1, start.1) > tolerance {
            print("\(pt(start.0))..\(pt(last.0))  (\(pt(last.0 - start.0 + 1)) \(coordinateUnit))  \(hex(start.1))")
            start = sample
        }
        last = sample
    }
    print("\(pt(start.0))..\(pt(last.0))  (\(pt(last.0 - start.0 + 1)) \(coordinateUnit))  \(hex(start.1))")
}

/// Content bands: lines where some pixel differs from the line's first pixel (the background).
func bands(count: Int, origin: Int, isContent: (Int) -> Bool) {
    var start: Int?
    var found = 0
    for i in 0..<count {
        if isContent(i) { if start == nil { start = i } }
        else if let s = start {
            print("\(pt(s + origin))..\(pt(i + origin))  size \(pt(i - s))"); start = nil; found += 1
        }
    }
    if let s = start { print("\(pt(s + origin))..\(pt(count + origin))  size \(pt(count - s))") }
    if found == 0 && start == nil { print("no content") }
}

switch command {
case "info":
    if declaredScale { print("\(bitmap.width) x \(bitmap.height) px = \(pt(bitmap.width)) x \(pt(bitmap.height)) pt at scale \(String(format: "%g", scale))") }
    else { print("\(bitmap.width) x \(bitmap.height) px; logical scale unknown") }
case "color":
    for pair in stride(from: 0, to: rest.count - 1, by: 2) {
        print("\(rest[pair]),\(rest[pair + 1])  \(hex(bitmap.pixel(px(rest[pair]), px(rest[pair + 1]))))")
    }
case "hline":
    let y = px(rest[0])
    let x0 = rest.count > 2 ? px(rest[1]) : 0, x1 = rest.count > 2 ? px(rest[2]) : bitmap.width - 1
    runs((x0...x1).map { ($0, bitmap.pixel($0, y)) })
case "vline":
    let x = px(rest[0])
    let y0 = rest.count > 2 ? px(rest[1]) : 0, y1 = rest.count > 2 ? px(rest[2]) : bitmap.height - 1
    runs((y0...y1).map { ($0, bitmap.pixel(x, $0)) })
case "rows":
    let x0 = px(rest[0]), x1 = px(rest[1])
    let y0 = rest.count > 3 ? px(rest[2]) : 0, y1 = rest.count > 3 ? px(rest[3]) : bitmap.height
    let background = bitmap.pixel(x0, y0)
    print("background \(hex(background))")
    var offset = y0
    bands(count: y1 - y0, origin: y0) { i in
        offset = y0 + i
        return (x0..<x1).contains { distance(bitmap.pixel($0, offset), background) > tolerance }
    }
case "cols":
    let y0 = px(rest[0]), y1 = px(rest[1])
    let x0 = rest.count > 3 ? px(rest[2]) : 0, x1 = rest.count > 3 ? px(rest[3]) : bitmap.width
    let background = bitmap.pixel(x0, y0)
    print("background \(hex(background))")
    bands(count: x1 - x0, origin: x0) { i in
        (y0..<y1).contains { distance(bitmap.pixel(x0 + i, $0), background) > tolerance }
    }
case "palette":
    let x = rest.count >= 4 ? px(rest[0]) : 0, y = rest.count >= 4 ? px(rest[1]) : 0
    let w = rest.count >= 4 ? px(rest[2]) : bitmap.width, h = rest.count >= 4 ? px(rest[3]) : bitmap.height
    var counts: [String: Int] = [:]
    for yy in stride(from: y, to: y + h, by: 1) {
        for xx in stride(from: x, to: x + w, by: 1) {
            let c = bitmap.pixel(xx, yy)
            counts[hex((c.0 / 4 * 4, c.1 / 4 * 4, c.2 / 4 * 4)), default: 0] += 1
        }
    }
    let total = Double(w * h)
    for (color, n) in counts.sorted(by: { $0.value > $1.value }).prefix(12) {
        print("\(color)  \(String(format: "%.1f", Double(n) / total * 100))%")
    }
case "ink":
    guard rest.count >= 4 else { print("ink needs x y w h"); exit(1) }
    let x = px(rest[0]), y = px(rest[1]), w = px(rest[2]), h = px(rest[3])
    let background = bitmap.pixel(x, y)
    var counts: [String: Int] = [:]
    var darkest = background
    var darkness = 0.0
    for yy in y..<(y + h) {
        for xx in x..<(x + w) {
            let c = bitmap.pixel(xx, yy)
            let d = distance(c, background)
            guard d > 90 else { continue }
            counts[hex((c.0 / 4 * 4, c.1 / 4 * 4, c.2 / 4 * 4)), default: 0] += 1
            if d > darkness { darkness = d; darkest = c }
        }
    }
    print("background \(hex(background))  strongest \(hex(darkest))")
    for (color, n) in counts.sorted(by: { $0.value > $1.value }).prefix(4) { print("\(color)  \(n) px") }
case "crop":
    let rect = CGRect(x: px(rest[0]), y: px(rest[1]), width: px(rest[2]), height: px(rest[3]))
    let zoom = rest.count > 5 ? Double(rest[5]) ?? 1 : 1
    guard let source = CGImageSourceCreateWithURL(URL(fileURLWithPath: args[1]) as CFURL, nil),
          let image = CGImageSourceCreateImageAtIndex(source, 0, nil),
          let cropped = image.cropping(to: rect) else { print("cannot crop"); exit(1) }
    let desiredWidth = rect.width * zoom, desiredHeight = rect.height * zoom
    guard desiredWidth.isFinite, desiredHeight.isFinite,
          desiredWidth >= 1, desiredHeight >= 1,
          desiredWidth <= 16_384, desiredHeight <= 16_384,
          abs(desiredWidth.rounded() - desiredWidth) < 0.000_001,
          abs(desiredHeight.rounded() - desiredHeight) < 0.000_001 else {
        print("zoom must produce bounded whole-pixel output dimensions"); exit(2)
    }
    let outputWidth = Int(desiredWidth), outputHeight = Int(desiredHeight)
    guard outputWidth * outputHeight <= 40_000_000,
          let context = CGContext(data: nil, width: outputWidth, height: outputHeight,
                                  bitsPerComponent: 8, bytesPerRow: outputWidth * 4,
                                  space: CGColorSpace(name: CGColorSpace.sRGB)!,
                                  bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else {
        print("cannot allocate bounded pixel crop"); exit(2)
    }
    context.interpolationQuality = .none
    context.draw(cropped, in: CGRect(x: 0, y: 0, width: outputWidth, height: outputHeight))
    guard let image = context.makeImage(),
          let destination = CGImageDestinationCreateWithURL(URL(fileURLWithPath: rest[4]) as CFURL,
                                                           "public.png" as CFString, 1, nil) else {
        print("cannot create crop output"); exit(1)
    }
    CGImageDestinationAddImage(destination, image, nil)
    guard CGImageDestinationFinalize(destination),
          let check = CGImageSourceCreateWithURL(URL(fileURLWithPath: rest[4]) as CFURL, nil),
          let verified = CGImageSourceCreateImageAtIndex(check, 0, nil),
          verified.width == outputWidth, verified.height == outputHeight else {
        print("crop output failed exact pixel-dimension verification"); exit(1)
    }
    print("wrote \(rest[4])")
default:
    print("unknown command \(command)"); exit(1)
}
