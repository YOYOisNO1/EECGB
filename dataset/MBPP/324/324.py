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
# Write a function to extract the sum of alternate chains of tuples.
#
# SOLUTION CODE
# ============================================
def sum_of_alternates(test_tuple):

  sum1 = 0

  sum2 = 0

  for idx, ele in enumerate(test_tuple):

    if idx % 2:

      sum1 += ele

    else:

      sum2 += ele

  return ((sum1),(sum2)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tuple, expected):
    try:
        if validate_solution(sum_of_alternates(
            test_tuple),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



