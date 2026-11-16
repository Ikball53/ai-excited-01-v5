"""Mending the Moon — make.fun ai-excited-01 entry.

Reads the entry image that sits beside this file and places an
exact copy of it at /output/entry.png, so the graded artwork is
the approved moon image, byte for byte.
"""

from pathlib import Path


def main() -> None:
    # Resolve from this file's own folder, so the caller's cwd never matters.
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise SystemExit(f"entry image not found beside main.py: {source}")
    target_dir = Path("/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(source.read_bytes())
    print(f"Wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
