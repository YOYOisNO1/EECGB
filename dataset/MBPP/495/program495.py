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
# Write a function to remove lowercase substrings from a given string by using regex.
#
# SOLUTION CODE
# ============================================
import re

def remove_lowercase(str1):

  remove_lower = lambda text: re.sub('[a-z]', '', text)

  result =  remove_lower(str1)

  return (result)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(remove_lowercase(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



