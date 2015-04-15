#!/usr/bin/env python

from tempfile import NamedTemporaryFile
from xml.parsers.xmlproc import xmlproc

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
