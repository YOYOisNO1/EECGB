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
# Write a function to move all zeroes to the end of the given array.
#
# SOLUTION CODE
# ============================================
def re_order(A):

    k = 0

    for i in A:

        if i:

            A[k] = i

            k = k + 1

    for i in range(k, len(A)):

        A[i] = 0

    return A

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, expected):
    try:
        if validate_solution(re_order(
            a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



