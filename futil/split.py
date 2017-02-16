#!/usr/bin/env python
# -"- coding: utf-8 -"-

from __future__ import unicode_literals


def get_data_parts(data, sizes):
    """Split the data into parts, given the parts' proportional sizes.
    @param data: the data to be split
    @param sizes: parts' sizes ratios
    @return a list of data parts
    """
    parts = []
    total_parts = sum(sizes)
    sizes = [int(round((part / float(total_parts)) * len(data))) for part in sizes]
    sizes[0] += len(data) - sum(sizes)  # 1st part takes the rounding error
    offset = 0
    for size in sizes:
        part = data[offset:offset + size]
        offset += size
        parts.append(part)
    return parts



