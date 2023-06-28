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
# Write a function to check whether the entered number is greater than the elements of the given array.
#
# SOLUTION CODE
# ============================================
def check_greater(arr, number):

  arr.sort()

  if number > arr[-1]:

    return ('Yes, the entered number is greater than those in the array')

  else:

    return ('No, entered number is less than those in the array')

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, number, expected):
    try:
        if validate_solution(check_greater(
            arr, number),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



