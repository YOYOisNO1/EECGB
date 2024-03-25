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
# Write a function to check the given decimal with a precision of 2 by using regex.
#
# SOLUTION CODE
# ============================================
import re

def is_decimal(num):

  num_fetch = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")

  result = num_fetch.search(num)

  return bool(result)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num, expected):
    try:
        if validate_solution(is_decimal(
            num),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



