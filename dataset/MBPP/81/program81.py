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
# Write a function to zip the two given tuples.
#
# SOLUTION CODE
# ============================================
def zip_tuples(test_tup1, test_tup2):

  res = []

  for i, j in enumerate(test_tup1):

    res.append((j, test_tup2[i % len(test_tup2)])) 

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup1, test_tup2, expected):
    try:
        if validate_solution(zip_tuples(
            test_tup1, test_tup2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



