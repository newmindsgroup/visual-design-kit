# Handoff to SwiftUI and Jetpack Compose

Version-Timestamp: 2026-10-20 02:08:24 UTC

Map the kit's DTCG tokens (names fixed by the token contract, built by `library/scripts/tokens.py` from `library/tokens/src/`) to native themes so iOS, Android and web share one source. All code below is **illustrative, not compiled here**: it shows structure and API choices, and must be built and tested in the target project.

## Pipeline

1. Source of truth: `library/tokens/src/*.tokens.json` (primitives, semantic light/dark/high-contrast, components, brands).
2. Build: `tokens.py build` emits `dist/tokens.resolved.json` with every alias resolved per mode and brand.
3. Generate platform files from the resolved JSON (Style Dictionary, a small script, or the project's own generator): an Xcode asset catalog plus a Swift file, and a Kotlin theme file. Never hand-copy hex values into Swift or Kotlin.
4. Check: render the same screen on web, iOS simulator and Android emulator in light, dark and high contrast and compare.

## Units

| Kit unit | iOS | Android | Rule |
| --- | --- | --- | --- |
| 1px (layout) | 1pt | 1dp | Spacing, radius, sizes carry over 1:1 |
| 1rem type (16px) | 16pt base, but map to text styles | 16sp | Map type by role (below), not by raw size |
| `--size-target-comfortable` 44px | 44pt | 48dp | Android uses its own 48dp minimum |
| Durations (ms) | seconds (0.2) | ms (200) | Same values |

## Color role mapping

| Kit semantic token | SwiftUI (asset catalog color) | Compose Material 3 role |
| --- | --- | --- |
| `color.bg.canvas` | `bg/canvas` | `background` and `surface` |
| `color.bg.surface` | `bg/surface` | `surfaceContainerLow` |
| `color.bg.surface-raised` | `bg/surface-raised` | `surfaceContainer` or `surfaceContainerHigh` |
| `color.bg.sunken` | `bg/sunken` | `surfaceContainerLowest` (light) / `surfaceDim` (dark), check visually |
| `color.bg.inverse` / `color.fg.inverse` | `bg/inverse` / `fg/inverse` | `inverseSurface` / `inverseOnSurface` |
| `color.fg.default` | `fg/default` | `onSurface` |
| `color.fg.muted` | `fg/muted` | `onSurfaceVariant` |
| `color.fg.subtle` | `fg/subtle` | extended token (placeholder text only) |
| `color.border.subtle` / `default` | `border/subtle` / `border/default` | `outlineVariant` / `outline` |
| `color.border.strong` | `border/strong` | extended token |
| `color.accent.default` | App accent color (`AccentColor`) | `primary` |
| `color.fg.on-accent` | `fg/on-accent` | `onPrimary` |
| `color.accent.subtle` / `color.accent.fg` | `accent/subtle` / `accent/fg` | `primaryContainer` / `onPrimaryContainer` |
| `color.danger.fg` / `bg` | `danger/fg` / `danger/bg` | `error` / `errorContainer` (and `onErrorContainer`) |
| `color.success.*`, `warning.*`, `info.*` | `success/fg` etc. | extended tokens (M3 has no success or warning roles) |
| `color.focus-ring` | `focus-ring` | extended token |
| `color.overlay-scrim` | `overlay-scrim` | `scrim` |

The paths match `library/tokens/src/semantic.*.tokens.json` as built on 2026-10-20 (`color.bg.canvas` is `--color-bg-canvas`); `tokens.resolved.json` carries the resolved value per mode and brand. Secondary and tertiary M3 roles have no kit equivalent: generate them from the brand's secondary hue or alias them to neutral roles.

On iOS, keep system chrome on system colors (`label`, `systemBackground`, Liquid Glass bars) and apply kit colors to the content layer and the accent. Replacing every system color with brand values breaks Increase Contrast and future OS changes.

## Typography role mapping

| Kit role (size) | iOS text style | Compose role |
| --- | --- | --- |
| Display (`5xl` 60 / `4xl` 48) | custom size relative to `.largeTitle` | `displayLarge` 57sp / `displayMedium` 45sp |
| Page title (`3xl` 36) | `.largeTitle` 34pt | `displaySmall` 36sp |
| Section title (`2xl` 30) | `.title` 28pt | `headlineMedium` 28sp |
| Subsection (`xl` 24) | `.title2` 22pt | `headlineSmall` 24sp |
| Card title (`lg` 20) | `.title3` 20pt | `titleLarge` 22sp |
| Body (`md` 16) | `.body` 17pt | `bodyLarge` 16sp |
| Secondary (`sm` 14) | `.subheadline` 15pt or `.footnote` 13pt | `bodyMedium` 14sp |
| Caption and labels (`xs` 12) | `.caption` 12pt | `bodySmall` 12sp / `labelMedium` 12sp |

Keep each platform's native body size (17pt iOS, 16sp Android). Line heights come from the text styles on iOS and from the M3 roles on Android, not from `--line-height-*`.

## SwiftUI: colors, custom fonts with Dynamic Type, spacing

Asset catalog color sets: set Appearances to "Any, Dark" and enable High Contrast, giving four variants (light, dark, light high-contrast, dark high-contrast). Fill them from the semantic light, dark and high-contrast sets. If the kit's high-contrast set has one polarity, decide which variant it fills and contrast-check the other.

```swift
// Illustrative, not compiled here.
import SwiftUI

enum KitColor {
    static let bgCanvas = Color("bg/canvas")
    static let bgSurface = Color("bg/surface")
    static let fgDefault = Color("fg/default")
    static let fgMuted = Color("fg/muted")
}

enum KitSpace {               // --space-* on a 4pt base
    static let s2: CGFloat = 8
    static let s3: CGFloat = 12
    static let s4: CGFloat = 16
}

extension Font {
    // Custom fonts must scale with Dynamic Type: always pass relativeTo.
    // Meridian brand: body Source Sans 3, display Schibsted Grotesk (both OFL, bundled with their licenses).
    static let kitBody = Font.custom("SourceSans3-Regular", size: 17, relativeTo: .body)
    static let kitTitle = Font.custom("SchibstedGrotesk-SemiBold", size: 28, relativeTo: .title)
}

struct BalanceRow: View {
    @ScaledMetric(relativeTo: .body) private var iconSize: CGFloat = 20   // grows with text
    @Environment(\.dynamicTypeSize) private var typeSize

    var body: some View {
        let layout = typeSize.isAccessibilitySize
            ? AnyLayout(VStackLayout(alignment: .leading, spacing: KitSpace.s2))
            : AnyLayout(HStackLayout(spacing: KitSpace.s3))
        layout {
            Image(systemName: "creditcard").frame(width: iconSize, height: iconSize)
            Text("Available balance").font(.kitBody).foregroundStyle(KitColor.fgMuted)
        }
        .padding(KitSpace.s4)
        .background(KitColor.bgSurface, in: .rect(cornerRadius: 12, style: .continuous))
    }
}
```

- Register bundled fonts in Info.plist (`UIAppFonts`) and ship their OFL license file. In UIKit use `UIFontMetrics(forTextStyle:).scaledFont(for:)` and `adjustsFontForContentSizeCategory = true`.
- Support Bold Text: provide a heavier weight when `legibilityWeight == .bold`.
- Motion: `--ease-standard` is `.timingCurve(0.2, 0, 0, 1, duration: 0.2)`; prefer system springs (`.smooth`, `.snappy`) for interactive motion. Read `accessibilityReduceMotion` and switch to fades.

## Jetpack Compose: color scheme, extended tokens, typography

```kotlin
// Illustrative, not compiled here. KitTokens.* is generated from tokens.resolved.json.
private val KitLight = lightColorScheme(
    primary = KitTokens.Light.AccentDefault,
    onPrimary = KitTokens.Light.FgOnAccent,
    primaryContainer = KitTokens.Light.AccentSubtle,
    onPrimaryContainer = KitTokens.Light.AccentFg,
    background = KitTokens.Light.BgCanvas,
    surface = KitTokens.Light.BgCanvas,
    surfaceContainerLow = KitTokens.Light.BgSurface,
    surfaceContainer = KitTokens.Light.BgSurfaceRaised,
    onSurface = KitTokens.Light.FgDefault,
    onSurfaceVariant = KitTokens.Light.FgMuted,
    outline = KitTokens.Light.BorderDefault,
    outlineVariant = KitTokens.Light.BorderSubtle,
    error = KitTokens.Light.DangerFg,
    errorContainer = KitTokens.Light.DangerBg,
    scrim = KitTokens.Light.OverlayScrim,
)
// KitDark, KitExtendedLight and KitExtendedDark are built the same way from the dark set.

@Immutable
data class KitExtendedColors(
    val fgSubtle: Color, val borderStrong: Color, val focusRing: Color,
    val successFg: Color, val successBg: Color, val warningFg: Color, val warningBg: Color,
)
val LocalKitColors = staticCompositionLocalOf<KitExtendedColors> { error("KitTheme missing") }

private val BrandSans = FontFamily(          // Meridian body family: Source Sans 3 (OFL)
    Font(R.font.source_sans_3_regular, FontWeight.Normal),
    Font(R.font.source_sans_3_semibold, FontWeight.SemiBold),
)
private val KitTypography = Typography(
    bodyLarge = TextStyle(fontFamily = BrandSans, fontSize = 16.sp, lineHeight = 24.sp),
    titleLarge = TextStyle(fontFamily = BrandSans, fontWeight = FontWeight.SemiBold, fontSize = 22.sp, lineHeight = 28.sp),
)
private val KitShapes = Shapes(
    extraSmall = RoundedCornerShape(4.dp), small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp), large = RoundedCornerShape(16.dp),
)

@Composable
fun KitTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    useDynamicColor: Boolean = false,          // brand apps default to false; offer it as a setting
    content: @Composable () -> Unit,
) {
    val context = LocalContext.current
    val scheme = when {
        useDynamicColor && Build.VERSION.SDK_INT >= 31 ->
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        darkTheme -> KitDark
        else -> KitLight
    }
    CompositionLocalProvider(LocalKitColors provides if (darkTheme) KitExtendedDark else KitExtendedLight) {
        MaterialTheme(colorScheme = scheme, typography = KitTypography, shapes = KitShapes, content = content)
    }
}
```

- Text sizes in `sp` only, so font scale applies; layout in `dp`. Never set `fontSize` in `dp`.
- Kit radius maps to M3 shapes: `sm` 4 = extraSmall, `md` 8 = small, `lg` 12 = medium, `xl` 16 = large; dialogs and sheets keep M3's 28dp extra-large.
- Kit shadows become tonal elevation on Android: `shadow-sm` level 1, `md` level 2, `lg` level 3, `xl` level 4-5.
- Motion: `tween(200, easing = CubicBezierEasing(0.2f, 0f, 0f, 1f))` equals `--duration-moderate` with `--ease-standard`; or use `MaterialTheme.motionScheme` springs (Compose Material 3 1.5).

## Dark mode and high contrast

| Mode | iOS | Android |
| --- | --- | --- |
| Light and dark | Asset catalog appearances follow the system; preview both | `isSystemInDarkTheme()` chooses the scheme; offer an in-app override only if users ask for it |
| High contrast | High Contrast variants in the asset catalog; `colorSchemeContrast == .increased` for custom drawing | User contrast setting (Android 14+, `UiModeManager.getContrast()`); ship medium and high schemes (verify API details) |
| Dynamic color | Not applicable | Optional; test kit extended colors next to wallpaper-derived roles for clashes |
| Reduced transparency | Glass becomes more opaque; check custom glass | Not applicable |

## Handoff checklist

- Token version and mode list recorded; generated files committed, never edited by hand.
- Every screen spec names semantic tokens and text roles, not hex or point sizes.
- Largest text size (AX5, 200% font scale), dark, high contrast and RTL renders attached.
- Custom font licenses included; SF Pro not used on Android.
- Code Connect (template files) or a component map links Figma components to the SwiftUI views and composables; see the `design-system` skill's Figma reference. The `figma-swiftui` skill helps translate Figma frames into SwiftUI when the Figma MCP server is connected.
