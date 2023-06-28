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
# Write a function to trim each tuple by k in the given tuple list.
#
# SOLUTION CODE
# ============================================
def trim_tuple(test_list, K):

  res = []

  for ele in test_list:

    N = len(ele)

    res.append(tuple(list(ele)[K: N - K]))

  return (str(res)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, k, expected):
    try:
        if validate_solution(trim_tuple(
            test_list, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



