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
# Write a python function to check whether the given array is monotonic or not.
#
# SOLUTION CODE
# ============================================
def is_monotonic(A): 

    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or

            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, expected):
    try:
        if validate_solution(is_monotonic(
            a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



