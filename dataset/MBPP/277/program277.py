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
# Write a function to filter a dictionary based on values.
#
# SOLUTION CODE
# ============================================
def dict_filter(dict,n):

 result = {key:value for (key, value) in dict.items() if value >=n}

 return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(dict, n, expected):
    try:
        if validate_solution(dict_filter(
            dict, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



