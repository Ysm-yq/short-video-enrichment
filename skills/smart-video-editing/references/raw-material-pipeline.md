# Raw material pipeline

## Intake manifest

Create `01_intake/assets.json` with one record per file:

```json
{
  "path": "C:/absolute/path/clip.mp4",
  "type": "video",
  "duration": 4.2,
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "audio_level_db": -42.1,
  "sha256": "...",
  "phash": "...",
  "group": "scene-03",
  "status": "candidate"
}
```

Use the bundled inventory helper for exact duplicates. Similarity analysis is a separate step: perceptual hashes identify candidates for comparison, not automatic rejection. Inspect different actions, expressions and audio before choosing. Keep a `duplicates.csv` explaining selection while preserving all originals.

## Local pre-analysis

Generate 360p proxies and a contact sheet. Use local measurements for blur/black-frame/silence flags. Use one bounded visual analysis pass on the contact sheet or proxy, with the theme and BF attached. Do not send all original files repeatedly.

## Candidate selection

Score each candidate against the brief using visible evidence:

- theme relevance;
- subject clarity;
- action or reaction;
- visual variety;
- technical quality;
- overlap with already selected material.

Keep the score and reason in `02_selection/shot_candidates.json`. A low score is not permission to invent a missing scene; mark the requirement as uncovered.

## Rough-cut handoff

After JianYing Smart Rough Cut, export or capture a proxy and create `03_roughcut/roughcut_manifest.json` with source ranges, order, and notes. Treat this sequence as the picture source for the final enrichment pass. Keep the original asset manifest so later revisions can recover a rejected shot without rescanning the whole folder.
