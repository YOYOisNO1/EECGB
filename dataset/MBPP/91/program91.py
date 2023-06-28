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
# Write a function to check if a substring is present in a given list of string values.
#
# SOLUTION CODE
# ============================================
def find_substring(str1, sub_str):

   if any(sub_str in s for s in str1):

       return True

   return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, sub_str, expected):
    try:
        if validate_solution(find_substring(
            str1, sub_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



