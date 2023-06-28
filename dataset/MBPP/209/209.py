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
# Write a function to delete the smallest element from the given heap and then insert a new item.
#
# SOLUTION CODE
# ============================================
import heapq as hq

def heap_replace(heap,a):

  hq.heapify(heap)

  hq.heapreplace(heap, a)

  return heap

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(heap, a, expected):
    try:
        if validate_solution(heap_replace(
            heap, a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



