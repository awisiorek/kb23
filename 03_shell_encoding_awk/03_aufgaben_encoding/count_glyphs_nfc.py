#!/usr/bin/env python
import sys
import unicodedata

print(len(unicodedata.normalize('NFC', sys.stdin.read())))