#!/usr/bin/env python
# $Id: split.py,v 2.2 2004/07/17 11:09:18 zeller Exp $

from itertools import combinations

def split(circumstances, n):
    subsets = []
    start = 0
    for i in range(0, n):
        len_subset = int((len(circumstances) - start) / float(n - i) + 0.5)
        subset = circumstances[start:start + len_subset]
        subsets.append(subset)
        start = start + len(subset)
    return subsets
