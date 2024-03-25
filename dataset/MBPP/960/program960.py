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
# Write a function to solve tiling problem.
#
# SOLUTION CODE
# ============================================
def get_no_ofways(n):

    if (n == 0):

        return 0;

    if (n == 1):

        return 1; 

    return get_no_ofways(n - 1) + get_no_ofways(n - 2);

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(get_no_ofways(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



