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
# Write a function to find the triplet with sum of the given array
#
# SOLUTION CODE
# ============================================
def check_triplet(A, n, sum, count):

    if count == 3 and sum == 0:

        return True

    if count == 3 or n == 0 or sum < 0:

        return False

    return check_triplet(A, n - 1, sum - A[n - 1], count + 1) or\

           check_triplet(A, n - 1, sum, count)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, sum, count, expected):
    try:
        if validate_solution(check_triplet(
            a, n, sum, count),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



