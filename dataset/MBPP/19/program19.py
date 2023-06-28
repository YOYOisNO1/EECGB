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
# Write a function to find whether a given array of integers contains any duplicate element.
#
# SOLUTION CODE
# ============================================
def test_duplicate(arraynums):

    nums_set = set(arraynums)    

    return len(arraynums) != len(nums_set)     

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arraynums, expected):
    try:
        if validate_solution(test_duplicate(
            arraynums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



