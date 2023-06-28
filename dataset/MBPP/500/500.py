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
# Write a function to concatenate all elements of the given list into a string.
#
# SOLUTION CODE
# ============================================
def concatenate_elements(list):

  ans = ' '

  for i in list:

    ans = ans+ ' '+i

  return (ans) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list, expected):
    try:
        if validate_solution(concatenate_elements(
            list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



