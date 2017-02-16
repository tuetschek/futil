#!/usr/bin/env python
# -"- coding: utf-8 -"-

from __future__ import unicode_literals


def create_turns(dialogues, history_length):
    """Given a list of dialogues (list of lists), create context-response turns, with the given
    history length in contexts (0 = just the preceding utterance)."""

    data = []
    for dialogue in dialogues:
        for pos, resp in enumerate(dialogue[1:], start=1):
            context = ' <B> '.join(dialogue[max(0, pos - history_length - 1):pos])
            data.append((context, resp))
    return data
