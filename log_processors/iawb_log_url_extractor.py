#!/usr/bin/env python

# Name: IA WayBack logs URL extractor
# Decription: Takes the path in the log as input and extracts the requested URL.
#   It assumes that the 7th field of the log is supplied on the STDIN.
#   Ignores the lines that do not look like a URL.
#   For better canonicalization, it returns SURT form instead.
# Requirements: The system needs python and "surt" package installed.
# Author: Sawood Alam

import sys
import surt
import re

pattern = re.compile("http://web\.archive\.org/web/(\*|\d{14})/(.*)")

if __name__ == "__main__":
    for line in sys.stdin:
        m = re.match(pattern, line)
        suri = "-"
        try:
            suri = surt.surt(m.group(2), trailing_comma=True)
        except Exception:
            sys.stderr.write("Skipping: " + line)
        if suri != "-": # TODO: Skip more URIs such as "about" or "dns"
            sys.stdout.write(suri + "\n")
