#!/usr/bin/env python
# -"- coding: utf-8 -"-

from __future__ import unicode_literals
from __future__ import print_function

import codecs


def write_lines(file_name, lines):
    """Write lines to a file."""
    with codecs.open(file_name, 'wb', 'UTF-8') as fh:
        for line in lines:
            print(line, file=fh)



