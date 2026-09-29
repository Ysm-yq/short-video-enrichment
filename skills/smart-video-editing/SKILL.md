---
name: smart-video-editing
description: "Turn a folder of raw video and image materials plus a brief into a first-pass JianYing rough cut, then finish the selected cut with narration, synchronized captions, BGM, sound effects, flower text, decorations, and acceptance checks. Use when the user wants the full raw-material-to-short-video workflow."
metadata:
  short-description: 智能素材粗剪与短视频制作
---

# 智能素材粗剪与短视频制作

This skill owns the workflow from raw media to a finished short video. It builds on the public `short-video-enrichment` Skill for the final sound and graphics pass.

## Route and project contract

1. For any video task, read `hyperframes` first. Use its routing and final quality gates.
2. Read `jianying-editor` when creating or inspecting a JianYing draft. Put all project scripts under the user's project folder, never in a Skill directory.
3. Use `media-use` only when sourcing or generating media. Prefer user-provided or local assets.
4. The source folder is never modified. Create a project folder with manifests, proxies, drafts, previews, and versioned outputs.

The user supplies some or all of: a raw-material folder, a theme, a BF/brief/script, target platform, target duration, commercial constraints, and any must-use or must-avoid shots. The current message overrides project defaults.

## Token-efficient intake

Before asking a model to judge every clip:

- Enumerate video, image, audio, and document files locally.
- Probe duration, dimensions, frame rate, codec, audio level, and file creation time.
- Generate low-resolution proxy frames/contact sheets and perceptual hashes locally.
- Exact duplicates can share one analysis result. Group near-duplicates for review; compare actions, expressions and useful sound before selecting. Never delete source files.
- Group clips by scene/time and flag very short, blurry, black, or silent material.
- Read the brief and convert it into a shot checklist, must-have facts, forbidden claims, target duration, and viewer action.

Only send representative frames or a rough-cut proxy for semantic judgment. Do not repeatedly upload or inspect every full-resolution duplicate.

## Rough-cut stage

Use the installed JianYing desktop Smart Rough Cut as the preferred first pass when the app is available and the user asked for it. Import the deduplicated candidate set and the brief, generate a rough-cut draft, and save it under a named rough-cut version. Do not let the rough-cut stage silently decide the final narration, BGM, flower text, or commercial claims.

Before this stage, read [capability-check.md](references/capability-check.md). Verify native desktop control and the actual feature first. If unavailable, request a user-exported rough cut or approval for a script-assisted alternative. Do not invoke an unrelated external-model script as if it were the desktop feature. Preserve actual drafts and exports; record unavailable deliverables honestly.

Default execution continues automatically after rough cut. If the project profile sets `pause_after_rough_cut: true`, present the rough-cut preview and wait for the user's approval before the final pass.

## Final enrichment stage

Use the `short-video-enrichment` workflow for:

- fact-grounded spoken Chinese narration;
- confirmed voice selection and actual-duration subtitle timing;
- regular captions and yellow flower text;
- BGM loop/crossfade and ducking;
- useful original sound preservation;
- subject-matched decorations, optional white-outline cutouts, and restrained punch-ins;
- full decode, frame, timing, placement, and loudness acceptance.

For this stage prefer FFmpeg + JianYing TTS for speed and reproducibility. Use a fully editable JianYing final draft only when the user explicitly requires that deliverable. Keep the JianYing rough cut as the editable picture source either way.

## Selection rules

- Prefer shots that directly support the theme, have a clear subject, show an action or reaction, and add visual variety.
- Avoid near-identical clips, accidental camera movement, blocked faces, long idle sections, and clips that repeat a stronger moment.
- Preserve factual sequences and required brand/event items from the BF. Do not invent prices, dates, project names, or claims.
- Do not overuse transitions, stickers, or zooms. The final pass should make the selected story clearer, not hide a weak selection.

## Required deliverables

Save a machine-readable asset manifest, duplicate report, shot checklist, rough-cut draft/proxy, final MP4, ASS/SRT subtitles, JSON/CSV timing, voice files, final mix, BGM/SFX references, previews, and an acceptance report. Report the exact paths, the rough-cut route used, the final duration, and any unresolved assumption.

## Execution references

Read [raw-material-pipeline.md](references/raw-material-pipeline.md) for analysis and [project-config.md](references/project-config.md) for configuration. Run `python scripts/inventory.py RAW_FOLDER MANIFEST_JSON` using absolute paths; place output outside raw footage. The helper only probes and detects exact duplicates; it does not perform semantic selection.
