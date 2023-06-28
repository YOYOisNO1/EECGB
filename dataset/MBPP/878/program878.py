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
# Write a function to check if the given tuple contains only k elements.
#
# SOLUTION CODE
# ============================================
def check_tuples(test_tuple, K):

  res = all(ele in K for ele in test_tuple)

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tuple, k, expected):
    try:
        if validate_solution(check_tuples(
            test_tuple, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



