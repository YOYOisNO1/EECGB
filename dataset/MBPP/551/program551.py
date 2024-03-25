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
# Write a function to extract a specified column from a given nested list.
#
# SOLUTION CODE
# ============================================
def extract_column(list1, n):

   result = [i.pop(n) for i in list1]

   return result 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, n, expected):
    try:
        if validate_solution(extract_column(
            list1, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



