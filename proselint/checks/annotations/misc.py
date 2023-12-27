"""Annotation left in text.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      archaism
date:       2014-06-10 12:31:19
categories: writing
---

Annotation left in text.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text: str):
    """Check the text."""
    err = "annotations.misc"
    msg = "Annotation left in text."

    items = [
        "FIXME",
        "FIX ME",
        "TODO",
        "todo",
        "ERASE THIS",
        "FIX THIS",
    ]

    return existence_check(
        text, items, err, msg, ignore_case=False, join=True)
