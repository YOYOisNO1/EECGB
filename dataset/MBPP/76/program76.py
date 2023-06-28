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
# Write a python function to count the number of squares in a rectangle.
#
# SOLUTION CODE
# ============================================
def count_squares(m,n):

    if(n < m):

        temp = m

        m = n

        n = temp

    return ((m * (m + 1) * (2 * m + 1) / 6 + (n - m) * m * (m + 1) / 2))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(m, n, expected):
    try:
        if validate_solution(count_squares(
            m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



