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
# Write a function to combine two given sorted lists using heapq module.
#
# SOLUTION CODE
# ============================================
from heapq import merge

def combine_lists(num1,num2):

  combine_lists=list(merge(num1, num2))

  return combine_lists

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num1, num2, expected):
    try:
        if validate_solution(combine_lists(
            num1, num2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



