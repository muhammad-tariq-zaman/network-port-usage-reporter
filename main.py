"""Summarise listening ports from netstat-style output.

Usage: python3 main.py netstat.txt
Parses lines containing a local address and LISTEN state (TCP) or a
UDP local address, and reports each port once with its protocol and
how many sockets use it, lowest port first.
"""
import argparse, re, sys
from collections import Counter

LINE_RE = re.compile(r"^(TCP|UDP)\s+\S+:(\d+)\s", re.IGNORECASE)


def parse(lines):
    counts = Counter()
    for line in lines:
        match = LINE_RE.search(line.strip())
        if match:
            counts[(match.group(1).upper(), int(match.group(2)))] += 1
    return sorted(counts.items())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, encoding="utf-8", errors="replace") as f:
        for (proto, port), count in parse(f.read().splitlines()):
            print(f"{proto} {port}: {count} socket(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
