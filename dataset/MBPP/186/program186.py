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
# Write a function to search some literals strings in a string by using regex.
#
# SOLUTION CODE
# ============================================
import re

def check_literals(text, patterns):

  for pattern in patterns:

    if re.search(pattern,  text):

        return ('Matched!')

    else:

        return ('Not Matched!')

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, patterns, expected):
    try:
        if validate_solution(check_literals(
            text, patterns),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



