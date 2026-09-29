# Reuse, costs and acceptance

This package is an agent workflow, not a bundled one-command video editor. TTS providers, desktop control, renderers, fonts and media must be available separately. Run dependency checks only for the chosen route. Do not infer availability from another user's machine.

Cache each voice line by text + provider + voice + rate/settings; a filename such as 01_01.ogg is not a safe cache key after text edits. Cache visual analysis by source fingerprint + sampling settings and retain the shot map. Source changes invalidate affected analysis. Retain a stage ledger with completed work, asset hashes, commands and known limitations; read that ledger on resume rather than entire conversations.

Keep voice, BGM, SFX and retained source audio as separate stems before mixing. Check actual BGM audibility in speech pauses and the photo ending as well as speech clarity. Numerical loudness does not prove a good mix. Record what was listened to; do not claim listening based only on a meter. Review event boundaries for captions/decorations, not just midpoints. For fast or ambiguous actions inspect denser frames or the clip. Say “sampled throughout” when that is the actual review method.

Validate timestamps, source ranges, duration and sync. For fixed-picture CFR outputs compare frame count; for VFR use timestamps and presentation duration rather than forcing a new frame rate. Target duration tolerance should follow the brief and be recorded. Separate picture, audio and container duration tolerances.

Music/font availability does not establish redistribution rights. Store source/license notes; MIT covers this repository's original code/docs, not third-party media or fonts. Do not bundle private family media in examples.

No measured token-saving percentage exists. Skill text itself consumes context. Reusable scripts, cached assets, bounded logs and fewer revisions may reduce use. Track tokens only when actual task-level usage is available; account quota percentage cannot be treated as a task token counter. Compare like-for-like task scope/model/quality and report measured saving = (baseline - repeat) / baseline, with sample size and cached-token accounting. Track TTS/provider costs separately.
