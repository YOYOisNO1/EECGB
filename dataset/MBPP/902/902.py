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
# Write a function to combine two dictionaries by adding values for common keys.
#
# SOLUTION CODE
# ============================================
from collections import Counter

def add_dict(d1,d2):

   add_dict = Counter(d1) + Counter(d2)

   return add_dict

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(d1, d2, expected):
    try:
        if validate_solution(add_dict(
            d1, d2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



