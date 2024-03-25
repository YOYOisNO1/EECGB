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
# Write a function to find the frequency of each element in the given list.
#
# SOLUTION CODE
# ============================================
from collections import defaultdict 

def freq_element(test_tup):

  res = defaultdict(int)

  for ele in test_tup:

    res[ele] += 1

  return (str(dict(res))) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, expected):
    try:
        if validate_solution(freq_element(
            test_tup),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



