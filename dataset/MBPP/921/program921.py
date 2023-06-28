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
# Write a function to perform chunking of tuples each of size n.
#
# SOLUTION CODE
# ============================================
def chunk_tuples(test_tup, N):

  res = [test_tup[i : i + N] for i in range(0, len(test_tup), N)]

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, n, expected):
    try:
        if validate_solution(chunk_tuples(
            test_tup, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



