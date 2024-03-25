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
# Write a function to extract specified number of elements from a given list, which follow each other continuously.
#
# SOLUTION CODE
# ============================================
from itertools import groupby 

def extract_elements(numbers, n):

    result = [i for i, j in groupby(numbers) if len(list(j)) == n] 

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(numbers, n, expected):
    try:
        if validate_solution(extract_elements(
            numbers, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



