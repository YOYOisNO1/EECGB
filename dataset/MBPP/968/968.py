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
# Write a python function to find maximum possible value for the given periodic function.
#
# SOLUTION CODE
# ============================================
def floor_max(A,B,N):

    x = min(B - 1,N)

    return (A*x) // B

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, n, expected):
    try:
        if validate_solution(floor_max(
            a, b, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



