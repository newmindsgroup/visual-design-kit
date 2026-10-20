# Sound

Version-Timestamp: 2026-10-20 01:59:37 UTC

Sound is the most intrusive layer of motion design: it reaches people who are not looking and cannot be ignored. Use it where it adds information or real brand value, keep it consistent with the motion language, and never let it be the only carrier of meaning.

## When sound helps

| Situation | Sound? | Notes |
| --- | --- | --- |
| Confirming an action whose result is out of sight (payment at a terminal, message sent with the screen locked) | Yes | Short and positive, paired with a visual and haptic confirmation |
| Alerts that need attention away from the screen (timers, calls, critical alarms) | Yes | Distinct per urgency level, and the user can turn it off |
| Frequent, repetitive actions (typing, scrolling, toggles, list selection) | No | Fatigue sets in fast; leave keyboard clicks to the OS setting |
| Brand moments (first launch, ident, unboxing video) | Sparingly | Short, skippable, off by default on the web |
| Errors | Only for critical errors | Low-key tone; never comic or scolding |
| Shared and public spaces (retail screens, offices, transit) | Default silent | Design for silence; confirm the venue's audio rules |
| Web pages | Never autoplay sound | Browsers block autoplay with sound anyway; start muted with a visible unmute |
| Games, children's products, music products | Richer sound is fine | Always with volume and mute controls |

## Never sound-only information

- **WCAG 2.2 SC 1.4.2 Audio Control (Level A):** audio that plays automatically for more than 3 seconds needs a control to pause or stop it, or a volume control independent of the system volume.
- **SC 1.3.3 Sensory Characteristics (Level A):** instructions must not rely on sound alone ("continue after the tone").
- **SC 1.2.2 Captions (Prerecorded), Level A:** meaningful sounds in media get caption text ("[alarm beeping]").
- Every sound has a visual equivalent, and a haptic one where the platform supports it. Many people keep devices muted, are deaf or hard of hearing, or are in noisy places.

## UI sound design basics

- **Duration:** 50-300ms for taps and confirmations; 300-800ms for notifications; 1-4s for a sonic logo (a common range, not a rule).
- **Personality:** follow the motion language (see [motion system](motion-system.md)). Calm and precise brands use soft, pure tones with short decay and no reverb tail. Energetic brands use brighter plucks, rhythmic figures and upward motion.
- **Pitch direction:** rising for positive, open and complete; falling for negative, close and delete. This is a widespread convention, so keep it consistent within the set.
- **Frequency:** phone speakers reproduce little below about 200-300Hz. Put the identifying energy in the midrange (roughly 500Hz-5kHz) and test on the device speaker, not only on studio monitors.
- **One palette:** build the set from one instrument or synth patch and one key or scale with related intervals, so the sounds read as a family. Name them by role: `ui.confirm`, `ui.error`, `notify.message`.
- **Variation:** give very frequent sounds 2-3 subtle variants (about 1-2 semitones apart, or a slight timbre change) to avoid machine-gun repetition. This is common practice in games.
- **Sync with motion:** start the sound on the visual contact frame (the check completes, the card lands), not when the animation starts. Keep it within one frame at 30fps. For audio-video sync in broadcast, ITU-R BT.1359 puts detectability at roughly 45ms of audio lead and 125ms of audio lag; verify against the recommendation if you are specifying tolerances.
- **Haptics:** pair them on the same frame. iOS offers `UIImpactFeedbackGenerator`, `UISelectionFeedbackGenerator` and `UINotificationFeedbackGenerator`, plus Core Haptics for custom patterns. Android offers `HapticFeedbackConstants` (for example `CONFIRM` and `REJECT` on API 30+). Follow the platform's guidance (Apple HIG: Playing haptics; Material Design).

## Loudness and levels for UI sounds

- Match the set to itself: measure each sound with a momentary or short-term loudness meter and keep them within about 1-2 LU of each other, so no sound jumps out. Critical alerts may sit a little louder. This is common practice rather than a standard.
- Keep UI sounds clearly quieter than the product's content (voice, music, video), because users set the system volume for content.
- Leave true-peak headroom of -1 dBTP or lower, and avoid heavy limiting. Small speakers distort hot, dense sounds.
- Respect system state: on iOS, use the ambient audio session category so UI sounds follow the Ring/Silent switch; on Android, respect the user's sound settings; and offer an in-app sound toggle.
- Assets: keep 48kHz 24-bit WAV masters. Ship short compressed files (AAC or CAF on iOS, OGG on Android, AAC, MP3 or Opus on the web). Preload short sounds and use the Web Audio API on the web for low latency.
- Loudness targets for rendered video (streaming, broadcast, podcasts) are in [video and motion graphics](video-and-motion-graphics.md).

## Sonic branding

| Element | What it is | Defaults |
| --- | --- | --- |
| Sonic logo (mnemonic) | A short melodic or rhythmic signature | 1-4s; recognizable from the first 2-3 notes |
| Short version | A cut-down for pre-roll, app launch and notifications | Under 1s |
| Brand motif | The mnemonic's melody, usable inside music | Works in different tempos and instruments |
| UI sound set | Confirm, error, notify, message, start, stop | From one palette, matched levels |
| Music beds | Licensed or commissioned tracks for video | Sit under voice-over; consistent genre and tempo range |
| Voice | Voice-over casting or a synthetic voice | Matches the archetype; consistent across channels |

- Derive the sound from the strategy: the archetype sets energy and register, and the motion language sets attack and rhythm (soft attack and sparse notes for calm brands; bright, percussive and rhythmic for energetic ones).
- Make the mnemonic survive bad conditions: phone speakers, heavy compression, a noisy street and a two-second pre-roll.
- Reference anchors (study them, never copy): Intel's five-note mnemonic, Netflix's "ta-dum", Mastercard's sonic brand (2019), the McDonald's "I'm lovin' it" melody, the Mac startup chime.
- Rights: using existing music in video needs a sync license (for the composition) and a master license (for the recording). Stock libraries differ in per-project and subscription terms. Commissioned work needs an agreed buyout or royalty arrangement. Some jurisdictions register sound marks as trademarks (for example, the USPTO and EUIPO accept sound marks). Confirm with counsel for the specific use and territory.

## Sound in video and motion graphics

- Voice-over leads. Duck music under it so speech stays clearly intelligible (often around 10-15dB of reduction while voice plays, as a rule of thumb), and check on a phone speaker.
- Sound effects support motion: one whoosh per transition at most, a hit when an element lands, a riser before a reveal. A whoosh on every cut is a stock-template tell.
- Design for silence first: social video autoplays muted, so the message must work with captions and on-screen text alone (see [kinetic typography](kinetic-typography.md)).
- Keep the sonic logo's timing locked to the visual ident's resolve frame in every cut-down.

## Checklist

- [ ] Every sound has a visual equivalent, and a haptic one where available
- [ ] No autoplaying sound on the web; respects silent mode on mobile; an in-app toggle exists
- [ ] The set comes from one palette, with levels matched and true peak at -1 dBTP or lower
- [ ] Sounds start on contact frames and stay in sync after export
- [ ] Tested on a phone speaker, a laptop speaker and earbuds
- [ ] Rights and licenses recorded for every sound and music asset
