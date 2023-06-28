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
# Write a python function to count number of cubes of size k in a cube of size n.
#
# SOLUTION CODE
# ============================================
def no_of_cubes(N,K):

    No = 0

    No = (N - K + 1)

    No = pow(No, 3)

    return No

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, k, expected):
    try:
        if validate_solution(no_of_cubes(
            n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



