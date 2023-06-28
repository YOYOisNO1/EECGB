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
# Write a function which accepts an arbitrary list and converts it to a heap using heap queue algorithm.
#
# SOLUTION CODE
# ============================================
import heapq as hq

def raw_heap(rawheap):

  hq.heapify(rawheap)

  return rawheap

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(rawheap, expected):
    try:
        if validate_solution(raw_heap(
            rawheap),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



