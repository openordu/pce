#!/usr/bin/env python3
"""Normalize flat OKR entries to the nested okr-block shape.

The 3-branch PCE campaign produced two serialization deltas:
  - Clawson (BEGLPT) + Herman (CFKNOQRVWY)  ->  "okr": {objective, key_results, evidence}
  - Clawford (A,D,H,I,J,M,S)                ->  objective/key_results/evidence as FLAT top-level keys

This converts each flat entry into the nested shape, moving the three fields
into an `okr` block. Every other field stays byte-identical; files that already
carry a nested `okr` are left untouched. Idempotent: a second run is a no-op.
"""
import json, os, sys, glob, argparse

def load_entry(path):
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)

def save_entry(path, obj):
    # Match repo serialization: literal UTF-8 (no \uXXXX), 2-space indent.
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write('\n')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', default='.entries')
    ap.add_argument('--no', dest='dry', action='store_true', help='dry-run: report only')
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.dir, '*.json')))
    changed = 0
    skipped_nested = 0
    unexpected = 0
    tape = []

    for path in files:
        obj = load_entry(path)
        has_nested = isinstance(obj.get('okr'), dict) and 'objective' in obj['okr']
        has_flat = ('objective' in obj and 'key_results' in obj and 'evidence' in obj
                    and 'okr' not in obj)

        if has_nested:
            skipped_nested += 1
            continue

        if not has_flat:
            unexpected += 1
            tape.append("NESTED-OFF  %s (neither shape)" % os.path.basename(path))
            continue

        okr_block = {
            "objective": obj.pop('objective'),
            "key_results": obj.pop('key_results'),
            "evidence": obj.pop('evidence'),
        }
        obj['okr'] = okr_block       # trailing position, matches nested files
        if not args.dry:
            save_entry(path, obj)
        changed += 1
        tape.append("CONVERT  %s  %s" % (os.path.basename(path), obj.get('name', '?')))

    print("scanned  : %d" % len(files))
    print("nested   : %d  (already have okr block, untouched)" % skipped_nested)
    print("converted: %d  (flat -> nested okr)" % changed)
    print("unexpected: %d" % unexpected)
    print("DRY-RUN (no files written)" if args.dry else "files written.")
    print("--- tape (first 20) ---")
    for line in tape[:20]:
        print("  " + line)
    if len(tape) > 20:
        print("  ... (%d more)" % (len(tape) - 20))

    if not args.dry:
        remaining_flat = 0
        for path in files:
            obj = load_entry(path)
            if 'objective' in obj and 'okr' not in obj:
                remaining_flat += 1
        print("POST-CHECK flat remainder: %d" % remaining_flat)

    return 0 if unexpected == 0 else 1

if __name__ == '__main__':
    sys.exit(main())