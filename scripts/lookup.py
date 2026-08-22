#!/usr/bin/env python3
"""PCE entry source lookup.

Given an entry name, find and print the human source text window from the
primary PDF (Monaghan) and cross-reference from the supplementary (Koch),
both already extracted to .txt in ./sources.

The rewrite source is the printed encyclopedia text. We never decrypt the
.entries/*.json cyphertext/salt (they are permanently locked per GAF-237).

Usage: python3 scripts/lookup.py "Badb"
"""
import sys, re, unicodedata, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MYTH = os.path.join(BASE, "sources", "myth.txt")
CULTURE = os.path.join(BASE, "sources", "culture.txt")

def load(p):
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()

def norm(s):
    # strip diacritics, lower, collapse whitespace
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(s.lower().split())

def find_windows(text, name, window_chars=1600, maxhits=2):
    """Return text windows near lines whose normalized start matches the name."""
    if not text:
        return []
    nn = norm(name)
    lines = text.split("\n")
    hits = []
    for i, line in enumerate(lines):
        nl = norm(line)
        # heading = line starts with the name (optionally parenthetical alts)
        if nl.startswith(nn + " ") or nl == nn or nl.startswith(nn + "("):
            start = max(0, i - 1)
            # extend the window for a few lines (paragraph)
            end = min(len(lines), i + 25)
            chunk = "\n".join(lines[start:end])
            hits.append(chunk)
            if len(hits) >= maxhits:
                break
    return hits

def main():
    if len(sys.argv) < 2:
        print("usage: lookup.py <entry-name> [--culture]"); return 1
    name = sys.argv[1]
    fussy = "--culture" in sys.argv or "--supp" in sys.argv
    text = load(CULTURE if fussy else MYTH)
    src_label = "SUPPLEMENTARY (Koch, Encyclopical Celtic Culture)" if fussy else \
        "PRIMARY (Monaghan, Encyclopedia of Celtic Mythology and Folklore)"
    if text is None:
        print(f"ERROR: source text not found ({MYTH})"); return 2
    hits = find_windows(text, name)
    if not hits:
        print(f"NO_HIT: '{name}' not found in {src_label}")
        return 3
    print(f"SOURCE: {src_label}")
    for i, h in enumerate(hits):
        print(f"\n--- window {i+1} ---")
        print(h)
    return 0

if __name__ == "__main__":
    sys.exit(main())