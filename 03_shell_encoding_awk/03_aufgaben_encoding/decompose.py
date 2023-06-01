#!/usr/bin/env python
import sys
import unicodedata

print(unicodedata.normalize('NFD', sys.stdin.read()), end='')