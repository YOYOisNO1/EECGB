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
# Write a function to count total characters in a string.
#
# SOLUTION CODE
# ============================================
def count_charac(str1):

 total = 0

 for i in str1:

    total = total + 1

 return total

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(count_charac(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



