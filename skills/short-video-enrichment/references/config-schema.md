# Project configuration schema

Store a project profile as `short_video_enrichment.yaml` or JSON in the project folder. Paths must be absolute on Windows. Keep personal preferences in a local profile, not in a public repository.

```yaml
source_video: "C:/absolute/path/source.mp4"
project_dir: "C:/absolute/path/project"
brief_files: []
mode: execute            # execute or plan_first
preserve_picture_edit: true

voice:
  selection_required: true
  speaker: BV001_fast_streaming
  display_name: 小姐姐
  language: zh-CN

subtitle:
  regular_font: "MaoKenTangYuan (beta)"
  regular_color: "#FFFFFF"
  flower_color: "#FFE34A"
  regular_size_720p: 82
  regular_size_1080p: 123
  safe_height_ratio: 0.78
  outline: true

audio:
  preserve_original_if_useful: true
  bgm_paths: []
  allow_second_bgm: true
  duck_music_under_voice: true
  target_lufs: -16
  true_peak_db: -1.5

graphics:
  highlight_decoration_groups: 2-4
  ordinary_decoration_groups: 1-2
  person_cutout_highlights: 1-2
  white_outline: true
  punch_in: true

outputs:
  video_name: "final_enriched.mp4"
  save_timeline: true
  save_previews: true
```

Resolve the current request, project profile and confirmed user profile first. Ask only for unresolved choices or an explicitly requested audition; retain confirmed choices across projects. Store personal profiles outside the public repository. Example values do not mean a public user's choices are confirmed.
