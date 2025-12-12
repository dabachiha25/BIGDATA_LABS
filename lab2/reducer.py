#!/usr/bin/env python3
# mapper.py
# Lit STDIN, normalise en minuscules, extrait les "mots" et émet "mot<TAB>1"

import sys
import re
import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)


# regex pour capturer mots (lettres, chiffres, apostrophe)
WORD_RE = re.compile(r"[A-Za-z0-9']+")

def main():
    for line in sys.stdin:
        line = line.strip().lower()
        if not line:
            continue
        words = WORD_RE.findall(line)
        for w in words:
            # émettre mot<TAB>1
            print(f"{w}\t1")

if __name__ == "__main__":
    main()
