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
# Write a function to round the given number to the nearest multiple of a specific number.
#
# SOLUTION CODE
# ============================================
def round_num(n,m):

    a = (n //m) * m

    b = a + m

    return (b if n - a > b - n else a)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, m, expected):
    try:
        if validate_solution(round_num(
            n, m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



