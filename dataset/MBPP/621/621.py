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
# Write a function to increment the numeric values in the given strings by k.
#
# SOLUTION CODE
# ============================================
def increment_numerics(test_list, K):

  res = [str(int(ele) + K) if ele.isdigit() else ele for ele in test_list]

  return res 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, k, expected):
    try:
        if validate_solution(increment_numerics(
            test_list, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



