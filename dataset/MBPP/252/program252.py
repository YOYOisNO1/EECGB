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
# Write a python function to convert complex numbers to polar coordinates.
#
# SOLUTION CODE
# ============================================
import cmath  

def convert(numbers):    

  num = cmath.polar(numbers)  

  return (num) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(numbers, expected):
    try:
        if validate_solution(convert(
            numbers),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



