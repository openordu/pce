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

def find_windows(text, name, maxhits=2):
    """Return text windows near a line whose heading matches the entry name.

    Matching is tiered:
    1. Exact heading "<Name> (": the name followed by space+open-paren, e.g.
       "Badb (Bave, Badhbh, Baobh, Badb Catha) Irish goddess".
    2. Cross-index heading: the name appears inside a heading's alt-spelling
       parenthetical, e.g. "Bran the Blessed (Bendigeidfran, ...)".
    3. Relaxed first-token heading, tolerating source spelling drift (Gwynn
       vs Gwyn).
    """
    if not text:
        return []
    nn = norm(name)
    lines = text.split("\n")
    hits = []

    def window(i):
        start = max(0, i - 1)
        end = min(len(lines), i + 30)
        return "\n".join(lines[start:end])

    # 1) exact heading "<Name> ("
    pat = re.compile(re.escape(nn) + r" \(")
    for i, line in enumerate(lines):
        if pat.search(norm(line)):
            hits.append(window(i))
            if len(hits) >= maxhits:
                return hits

    # 2) cross-index heading: name inside an alt-spelling parenthetical
    for i, line in enumerate(lines):
        nl = norm(line)
        if nn in nl and "(" in nl:
            hits.append(window(i))
            if len(hits) >= maxhits:
                return hits

    # 3) relaxed first-token heading (spelling drift)
    toks = nn.split()
    lead = re.escape(toks[0]) + r"+"
    rest = r"\s+".join(re.escape(t) for t in toks[1:])
    rpat = re.compile(r"\b" + lead + (r"\s+" + rest if rest else "") + r" \(")
    for i, line in enumerate(lines):
        if rpat.search(norm(line)):
            hits.append(window(i))
            if len(hits) >= maxhits:
                break
    return hits


def main():
    if len(sys.argv) < 2:
        print("usage: lookup.py <entry-name> [--culture]"); return 1
    name = sys.argv[1]
    fussy = "--culture" in sys.argv or "--supp" in sys.argv
    text = load(CULTURE if fussy else MYTH)
    src_label = "SUPPLEMENTARY (Koch, Encyclopedia of Celtic Culture)" if fussy else \
        "PRIMARY (Monaghan, Encyclopedia of Celtic Mythology and Folklore)"
    if text is None:
        print(f"ERROR: source text not found ({MYTH})"); return 2
    hits = find_windows(text, name)
    if not hits:
        print(f"NO_HIT: '{name}' not found in {src_label}")
        # primary absence is a real blocking signal (rc 4); supplementary
        # absence is informational (rc 3 — cross-reference is best-effort)
        return 3 if fussy else 4
    print(f"SOURCE: {src_label}")
    for i, h in enumerate(hits):
        print(f"\n--- window {i+1} ---")
        print(h)
    return 0

if __name__ == "__main__":
    sys.exit(main())