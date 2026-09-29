---
name: short-video-enrichment
description: Add spoken narration, synchronized subtitles, background music, flower text, stickers, and light motion accents to an already edited short video while preserving the original shot order and duration. Use for Chinese vertical family, travel, attraction, event, and lifestyle videos when the user wants a finished MP4 plus editable timing assets.
metadata:
  short-description: 短视频字幕配乐旁白增效剪辑
---

# Short Video Enrichment

Use this skill for an existing cut that needs a complete sound and graphic pass. The source edit is the user's picture lock: do not reorder, trim, or replace shots unless the user explicitly asks for a picture edit.

## Route and tools

1. For any video task, read the installed `hyperframes` skill first. Use its routing and quality gates.
2. For ordinary existing-footage enrichment, prefer a deterministic local pipeline: FFmpeg for compositing and mixing, and the installed JianYing TTS helper for voice generation. Put all project scripts in the user's project folder, never inside this Skill directory.
3. Use the `jianying-editor` workflow when the user explicitly wants an editable JianYing draft. Use Computer Use only when the user explicitly asks for UI operation.
4. Use `media-use` when sourcing or generating new media. Do not download a random online song when a local or user-provided track is available.

## Intake

Resolve the project directory, source video, optional brief/script documents, music, fonts, stickers, and reference images. If multiple videos are present, choose the explicitly named source; otherwise stop and ask which one. Read the brief before writing copy. Inspect metadata with `ffprobe`, sample the whole video at regular intervals, and measure whether the source audio contains useful speech or ambience.

Create a small project configuration before rendering. It records the confirmed voice, font, colors, caption position, decoration density, original-audio decision, music choice, and output paths. If the user says “直接执行”, use the saved defaults and do not pause for a plan. Reuse confirmed personal choices across projects. For first-use selection and explicit voice-choice requests, read [personalization.md](references/personalization.md).

## Personalizable defaults

The public Skill is configurable. The following profile is the reference style used by the owner's local version:

- Mood: warm, lively, cute, family-friendly, and persuasive enough to make viewers want to visit.
- Voice: Chinese female “小姐姐”; the exact provider/speaker ID is a configuration value, not a hard-coded public secret.
- Regular subtitles: rounded playful font, white fill, dark outline, bold enough for phone viewing.
- Flower text: yellow, larger than regular subtitles, with a brief pop or slide-in.
- Safe position: middle-lower area, normally around 76–80% of frame height; keep clear of faces, important subjects, and the platform bottom UI.
- Decoration density: 2–4 small decoration groups on highlight shots; 1–2 light accents on selected ordinary shots; never decorate every frame mechanically.
- Person emphasis: at most 1–2 memorable moments per short video receive a white-outline cutout and a restrained punch-in.
- Music: one main bed by default; use a second bed only when the emotional section really changes. Duck music under narration and restore it in pauses.

Treat these as defaults, not universal facts. A project profile or the user's current message overrides them.

## Copy and audio decisions

- Write short spoken Chinese that follows visible actions and creates a clear viewer arc: hook, concrete experiences, one or two memorable peaks, and a natural closing invitation.
- Do not invent prices, dates, animal names, project names, or commercial claims. Use the supplied brief or visible evidence; mark uncertain identification for review.
- If the original audio has useful cheers, laughter, animal sounds, or dialogue, preserve those portions and lower the music around them. If it is silent or distracting, replace it with narration/music only after inspecting it.
- Generate narration in short lines so each line can be retimed independently. Subtitle timing follows the actual generated voice duration, not a guessed reading speed.
- Mix for clear speech. Target an integrated final loudness near -16 LUFS and true peak no higher than -1.5 dBTP unless the user specifies another delivery standard.

## Graphics and motion

- Use the confirmed font file when available; if it is missing, report the fallback instead of silently substituting a visually unrelated font.
- Keep ordinary subtitles readable and stable. Flower text may animate, but it must not cover faces or the main action.
- Choose decorations from the subject: stars/sparkles for excitement, animal or harvest icons for themed scenes, speed lines for rides, moon/clouds for dreamy photo endings. Use restraint and vary placement.
- For a white-outline person sticker, derive it from a frame in the supplied video or a user-provided image, keep the original scene intact, and report that it is an overlay.

## Render and acceptance

Keep the source resolution, aspect ratio, frame rate, shot order, and duration. Render a new output file rather than overwriting the source. Save these project artifacts beside the output: final MP4, ASS and SRT subtitles, JSON/CSV timing table, individual voice files, final mix, chosen BGM, preview/contact sheet, and an acceptance report.

The final check must verify:

1. Output exists and decodes from beginning to end without errors.
2. Fixed-picture CFR output preserves frame count and cadence; VFR output is checked by timestamps and presentation duration. Investigate drift rather than forcing a frame rate.
3. Narration and subtitles align; no subtitle is clipped or placed in the platform danger zone.
4. Speech is intelligible, music does not mask it, and useful original sound remains audible.
5. Flower text, stickers, and decorations do not cover faces or important subjects.
6. The report names the exact output path and lists any unverified assumption, missing font, or licensing limitation.

## Related references

- Before production or revision, read [reuse-and-validation.md](references/reuse-and-validation.md) for cache invalidation, audible music checks and dependency boundaries.

- Read [config-schema.md](references/config-schema.md) when creating or updating a project configuration.
- Read [production-workflow.md](references/production-workflow.md) when executing a full render or a revision pass.
