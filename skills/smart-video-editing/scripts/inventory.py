from pathlib import Path
import json, subprocess, argparse, hashlib

MEDIA = {".mp4", ".mov", ".mkv", ".avi", ".m4v", ".webm", ".jpg", ".jpeg", ".png", ".webp", ".wav", ".mp3", ".m4a", ".ogg"}

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(description="Local inventory and exact duplicate detection; no uploads or source edits")
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    if not source.is_dir():
        ap.error("source must be a directory")
    if output == source or source in output.parents:
        ap.error("place the manifest outside the raw-material directory")
    old = {}
    if output.exists():
        previous = json.loads(output.read_text(encoding="utf-8"))
        if previous.get("source") == str(source):
            old = {r["path"]: r for r in previous.get("assets", [])}
    rows, seen = [], {}
    for p in sorted(source.rglob("*")):
        if p.is_symlink() or not p.is_file() or p.suffix.lower() not in MEDIA:
            continue
        stat = p.stat()
        sig = [stat.st_size, stat.st_mtime_ns]
        cached = old.get(str(p), {})
        if cached.get("signature") == sig and not cached.get("error"):
            row = dict(cached)
        else:
            row = {"path": str(p), "signature": sig, "sha256": digest(p)}
            try:
                result = subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(p)], capture_output=True, text=True, encoding="utf-8", timeout=120)
                if result.returncode:
                    row["error"] = result.stderr[-1000:]
                else:
                    data = json.loads(result.stdout)
                    row["duration"] = data.get("format", {}).get("duration")
                    row["streams"] = [{k: s[k] for k in ("codec_type", "codec_name", "width", "height", "avg_frame_rate", "r_frame_rate", "sample_rate") if k in s} for s in data.get("streams", [])]
            except (OSError, subprocess.TimeoutExpired, ValueError) as e:
                row["error"] = str(e)
        row.pop("exact_duplicate_of", None)
        if row["sha256"] in seen:
            row["exact_duplicate_of"] = seen[row["sha256"]]
        else:
            seen[row["sha256"]] = str(p)
        rows.append(row)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {"schema_version": 1, "source": str(source), "assets": rows,
               "limitations": "Exact file duplicates only. Similarity, blur, semantic selection and original-audio usefulness require separate inspection. Cache uses size and mtime."}
    tmp = output.with_name(output.name + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(output)
    print(json.dumps({"files": len(rows), "exact_duplicates": sum("exact_duplicate_of" in r for r in rows), "errors": sum("error" in r for r in rows), "manifest": str(output)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
