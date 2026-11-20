#!/usr/bin/env python3
"""Regenerate public pages, navigation, and search metadata in a fixed order.

Does not touch SWAAG source, perform network actions or publish. Run after
editing source templates before local regression tests and a GitHub push.
"""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
scripts=[
 'rebuild_software_home.py',
 'rebuild_software_page.py',
 'render_software_portfolio.py',
 'build_swaag_landing.py',
 'build_commercial_path.py',
 'market_differentiation.py',
 'align_software_navigation.py',
 'refresh_public_seo.py',
]
for filename in scripts:
 print('RUN',filename,flush=True)
 subprocess.run([sys.executable,str(root/'scripts'/filename)],cwd=root,check=True)
print('GENERATED existing portfolio and dedicated SWAAG page with consistent SEO metadata')
