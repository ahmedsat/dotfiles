#!/usr/bin/env python3

import sys

decoded = sys.argv[1].encode('latin-1').decode('cp1256')
print(decoded)

