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
# Write a function to merge multiple sorted inputs into a single sorted iterator using heap queue algorithm.
#
# SOLUTION CODE
# ============================================
import heapq

def merge_sorted_list(num1,num2,num3):

  num1=sorted(num1)

  num2=sorted(num2)

  num3=sorted(num3)

  result = heapq.merge(num1,num2,num3)

  return list(result)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num1, num2, num3, expected):
    try:
        if validate_solution(merge_sorted_list(
            num1, num2, num3),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



