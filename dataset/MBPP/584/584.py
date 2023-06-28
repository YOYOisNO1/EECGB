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
# Write a function to find all adverbs and their positions in a given sentence by using regex.
#
# SOLUTION CODE
# ============================================
import re

def find_adverbs(text):

  for m in re.finditer(r"\w+ly", text):

    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, expected):
    try:
        if validate_solution(find_adverbs(
            text),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



