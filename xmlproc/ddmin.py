#!/usr/bin/env python

from tempfile import NamedTemporaryFile
from xml.parsers.xmlproc import xmlproc
from split import split
from listsets import listminus
import re

PASS       = "PASS"
FAIL       = "FAIL"
UNRESOLVED = "UNRESOLVED"

def ddmin(circumstances, test):
    """Return a sublist of CIRCUMSTANCES that is a relevant configuration
       with respect to TEST."""

    assert test([]) == PASS
    assert test(circumstances) == FAIL

    n = 2
    while len(circumstances) >= 2:
        subsets = split(circumstances, n)
        assert len(subsets) == n

        some_complement_is_failing = 0
        for subset in subsets:
            complement = listminus(circumstances, subset)

            if test(complement) == FAIL:
                circumstances = complement
                n = max(n - 1, 2)
                some_complement_is_failing = 1
                break

        if not some_complement_is_failing:
            if n == len(circumstances):
                break
            n = min(n * 2, len(circumstances))

    return circumstances

def test(data):

    if not data:
        return PASS

    p = xmlproc.XMLProcessor()

    with NamedTemporaryFile(dir='/tmp', delete=False) as f:
        for i in data:
            f.write(i[1])
        filename = f.name

    try:
        p.parse_resource(filename)
        return PASS
    except UnboundLocalError as e:
        print("=====")
        print(''.join(i[1] for i in data))
        print("=====")
        return FAIL
    except:
        return UNRESOLVED

if __name__ == "__main__":

    def string_to_list(s):
        c = []
        for i in range(len(s)):
            c.append((i, s[i]))
        return c

    with open('demo/urls.xml') as f:
        data = f.read()

    circumstances = string_to_list(data)
    ddmin(circumstances, test)
