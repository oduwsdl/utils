#!/usr/bin/env python

# Name: IA WayBack logs URI-R extractor
# Decription: Takes the path in the log as input and extracts the URI-Rs.
#   It assumes that the 7th field of the log is supplied to the STDIN.
#   Ignores the lines that do not look like a URL.
#   For better canonicalization, it returns SURT form instead.
# Requirements: The system needs python and "surt" package installed.
# Usage:
#     STDIN | ./iawb_log_urir_extractor.py | STDOUT
#     STDIN | ./iawb_log_urir_extractor.py -q | STDOUT
#   Errors are written to the STDERR that can be supressed using -q flag
# Author: Sawood Alam

import sys
import surt
import re

if __name__ == "__main__":
    pattern = re.compile("http://web\.archive\.org/web/(\*|\d{14})/(.*)")
    # Supress error if -q flag is set
    if "-q" in sys.argv:
        sys.stderr = open('/dev/null', 'w')

    for line in sys.stdin:
        m = re.match(pattern, line)
        suri = "-"
        try:
            suri = surt.surt(m.group(2), trailing_comma=True)
        except Exception:
            sys.stderr.write("Skipping: " + line)
        if suri != "-": # TODO: Skip more URIs such as "about" or "dns"
            sys.stdout.write(suri + "\n")
