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
# Write a function to add two integers. however, if the sum is between the given range it will return 20.
#
# SOLUTION CODE
# ============================================
def sum_nums(x, y,m,n):

    sum_nums= x + y

    if sum_nums in range(m, n):

        return 20

    else:

        return sum_nums

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, m, n, expected):
    try:
        if validate_solution(sum_nums(
            x, y, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



