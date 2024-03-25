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
# Write a function to find the ascii value of a character.
#
# SOLUTION CODE
# ============================================
def ascii_value(k):

  ch=k

  return ord(ch)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(k, expected):
    try:
        if validate_solution(ascii_value(
            k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



