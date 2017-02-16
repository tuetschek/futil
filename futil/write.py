#!/usr/bin/env python
# -"- coding: utf-8 -"-

from __future__ import unicode_literals

import codecs


def write_lines(file_name, lines):
    """Write lines to a file."""
    with codecs.open(file_name, 'wb', 'UTF-8') as fh:
        for line in lines:
            print >> fh, line



