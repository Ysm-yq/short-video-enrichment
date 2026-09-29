# Capability and handoff checks

Desktop Smart Rough Cut is a preferred route, not a verified API. Before claiming it ran, record the installed app version, observed feature name, accepted inputs, actual output and successful export. Inspect whether it selects visual highlights or merely removes speech pauses; the latter is insufficient for family/travel montage selection. Do not assume it accepts a BF document.

Use only an available, supported desktop-control capability. If native app control is unavailable, say so and ask for a user-exported rough cut or consent to the script-assisted alternative. Do not repeatedly retry an unavailable capability.

The existing third-party smart_rough_cut.py is NOT the desktop feature. The inspected implementation uses an external model and a subject-specific prompt. The filename alone is not evidence of readiness. Do not invoke it unchanged, upload footage to an unconfirmed provider, or silently replace the requested desktop stage. A filename-only matching or round-robin fallback does not satisfy semantic selection.

Review the rough cut for brief coverage, duplicate actions, pacing, shot variety and target duration before enrichment. Inspect candidate clips omitted from the rough cut when a required scene is missing. Save source file, source in/out, destination start/end and selection reason. If only a flattened export exists, mark original source ranges unavailable rather than inventing them.

For the final pass, choose the existing tested renderer. FFmpeg suits measured narration, ASS captions and simple overlays; HyperFrames suits complex designed animation; an editable final JianYing draft is a separate deliverable and requires version compatibility checks. Honor applicable installed skill routing, without claiming HyperFrames rendered an FFmpeg output.
