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
# Write a function to find the nth octagonal number.
#
# SOLUTION CODE
# ============================================
def is_octagonal(n): 

	return 3 * n * n - 2 * n 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(is_octagonal(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



