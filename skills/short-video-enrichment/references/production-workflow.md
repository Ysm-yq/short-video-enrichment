# Production workflow

## 1. Inspect

Probe duration, dimensions, frame rate, frame count, codecs, and audio level. Sample the full video, not only the first few seconds. Build a shot/action map with approximate time ranges. Identify useful original sound and sections that need narration.

## 2. Plan

Create a timeline table with `start`, `end`, `visual_action`, `narration`, `subtitle`, `flower_text`, `decoration`, `audio_source`, and `notes`. Keep lines short enough to finish inside their assigned visual range. Resolve uncertain facts before rendering.

## 3. Generate voice and subtitles

Generate one audio file per narration line with the confirmed speaker. Measure each file, fit only within its assigned range, and derive subtitle events from the measured result. Keep ASS for styled output and SRT for portability.

## 4. Mix audio

Loop or crossfade the chosen BGM to the source duration. Preserve useful source audio. Duck the BGM under narration and real event sound. Normalize the final mix to the configured loudness target.

## 5. Add graphics

Place regular captions in the safe middle-lower zone. Add yellow flower text only for hooks, memorable actions, section changes, and the closing invitation. Add 2–4 decoration groups to highlight moments and 1–2 restrained accents to selected ordinary moments. Add cutout/punch-in overlays only when they clarify a real reaction.

## 6. Render and inspect

Render to a new filename. Decode the whole output. Check duration/frame count against the source. Generate representative preview frames, including every flower-text and cutout event. Review caption legibility, face clearance, audio balance, and the final call to action.

## 7. Revision mode

For a user correction, edit the timeline/configuration and rerun only the affected asset generation and render stages. Preserve the source and previous output. Report the new version path and the changed time ranges.
