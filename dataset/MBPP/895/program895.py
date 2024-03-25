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
# Write a function to find the maximum sum of subsequences of given array with no adjacent elements.
#
# SOLUTION CODE
# ============================================
def max_sum_subseq(A):

    n = len(A)

    if n == 1:

        return A[0]

    look_up = [None] * n

    look_up[0] = A[0]

    look_up[1] = max(A[0], A[1])

    for i in range(2, n):

        look_up[i] = max(look_up[i - 1], look_up[i - 2] + A[i])

        look_up[i] = max(look_up[i], A[i])

    return look_up[n - 1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, expected):
    try:
        if validate_solution(max_sum_subseq(
            a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



