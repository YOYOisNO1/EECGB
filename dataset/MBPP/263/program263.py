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
# Write a function to merge two dictionaries.
#
# SOLUTION CODE
# ============================================
def merge_dict(d1,d2):

 d = d1.copy()

 d.update(d2)

 return d

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(d1, d2, expected):
    try:
        if validate_solution(merge_dict(
            d1, d2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



