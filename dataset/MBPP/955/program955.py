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
# Write a function to find out, if the given number is abundant.
#
# SOLUTION CODE
# ============================================
def is_abundant(n):

    fctrsum = sum([fctr for fctr in range(1, n) if n % fctr == 0])

    return fctrsum > n

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(is_abundant(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



