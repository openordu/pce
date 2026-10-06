#!/usr/bin/env python3
"""Extract a Koch article from culture.txt given its \f-head start line.
Usage: python3 extract_article.py <start_line> <tag>"""
import re, sys
text = open('/home/hermes/code/openordu/pce-clawson/sources/culture.txt', encoding='utf-8', errors='replace').read()
lines = text.split('\n')
start = int(sys.argv[1])
tag = sys.argv[2] if len(sys.argv) > 2 else "ART"
# Article runs until the next line containing "\f" AND a [page] marker AND a headword
end = len(lines)
for i in range(start + 1, len(lines)):
    if "\f" in lines[i] and re.search(r"\[\d{3,4}\]", lines[i]):
        # confirm there's a headword token after the page marker (not a running head continuation)
        m = re.search(r"\[\d{3,4}\]\s*([A-Za-zÀ-ÿ'’ ,\.\-]+)", lines[i])
        if m:
            end = i
            break
print(f"===== {tag} :: lines {start}..{end} =====")
for i in range(start, end):
    print(lines[i])
