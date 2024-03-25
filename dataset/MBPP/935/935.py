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
# Write a function to calculate the sum of series 1²+2²+3²+….+n².
#
# SOLUTION CODE
# ============================================
def series_sum(number):

 total = 0

 total = (number * (number + 1) * (2 * number + 1)) / 6

 return total

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(number, expected):
    try:
        if validate_solution(series_sum(
            number),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



