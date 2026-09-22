#!/usr/bin/env python3
"""Show local readiness without calling any service."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.config import load_config


root = Path(__file__).resolve().parents[1]
skills = sorted(path.name for path in (root / "skills").iterdir() if path.is_dir())
settings = load_config({})
print(f"skills: {len(skills)}")
print(f"mode: {settings.mode}")
print("network: not contacted")
