#!/usr/bin/env python
# Script to fix nmath.h so that it prints error / warnings to stderr.
import os
import re
import sys

with open(sys.argv[1], "rt") as fp:
    for x in fp:
        if x.startswith('#define MATHLIB_ERROR'):
            # correct the printf -> fprintf(stderr,
            x = re.sub("printf\(", "fprintf(stderr,", x, count=1)

        elif x.startswith('#define MATHLIB_WARNING'):
            # correct the printf -> fprintf(stderr,
            x = re.sub("printf\(", "fprintf(stderr,", x, count=1)

        print(x, end='')
