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
# Write a function to remove the parenthesis area in a string.
#
# SOLUTION CODE
# ============================================
import re

def remove_parenthesis(items):

 for item in items:

    return (re.sub(r" ?\([^)]+\)", "", item))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(items, expected):
    try:
        if validate_solution(remove_parenthesis(
            items),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



