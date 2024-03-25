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
# Write a python function to check whether a given sequence is linear or not.
#
# SOLUTION CODE
# ============================================
def seq_linear(seq_nums):

  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]

  if len(set(seq_nums)) == 1: 

    return "Linear Sequence"

  else:

    return "Non Linear Sequence"

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(seq_nums, expected):
    try:
        if validate_solution(seq_linear(
            seq_nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



