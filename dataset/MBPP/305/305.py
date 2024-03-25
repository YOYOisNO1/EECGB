import array
import bisect
import collections
import datetime
import functools
import heapq
import itertools
import math
import queue
import re
import string
import sys
from typing import Any, Dict, List, Optional, Set

# Question Prompt (NOT what is passed to the model)
# Write a function to match two words from a list of words starting with letter 'p'.
#
# SOLUTION CODE
# ============================================
import re

def start_withp(words):

 for w in words:

        m = re.match("(P\w+)\W(P\w+)", w)

        if m:

            return m.groups()

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(words, expected):
    try:
        if validate_solution(start_withp(
            words),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



