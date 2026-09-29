# Full project configuration

```yaml
raw_material_dir: "C:/absolute/path/raw"
project_dir: "C:/absolute/path/project"
brief_files: []
theme: ""
target_duration_seconds: null
target_platform: douyin
mode: execute
pause_after_rough_cut: false
preserve_source_files: true

rough_cut:
  preferred_route: jianying_desktop_smart_rough_cut
  fallback_route: ask_for_export_or_alternative
  max_failures_before_fallback: 2
  create_proxy: true

enrichment:
  inherit_from: short-video-enrichment
  preserve_original_if_useful: true
  enable_voice: true
  enable_bgm: true
  enable_sfx: true
  enable_flower_text: true
  enable_decorations: true
  enable_person_cutout: true

outputs:
  save_asset_manifest: true
  save_duplicate_report: true
  save_roughcut_draft: true
  save_roughcut_proxy: true
  save_final_timeline: true
  save_acceptance_report: true
```

For the owner's local version, merge this file with `my-short-video-enrichment/profile.yaml`. The user's current request always wins.
