#!/usr/bin/env python3
"""News-image entry for 21 November 2026: copy the bundled front page
to the output directory as entry.png.

The image (entry.png, 1024 by 1024, drawn for Saturday 21 November 2026)
sits beside this file in the repository. Outside the grader,
MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
shutil.copyfile(os.path.join(here, "entry.png"),
                os.path.join(out_dir, "entry.png"))
