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
# Write a function to find the area of a rombus.
#
# SOLUTION CODE
# ============================================
def rombus_area(p,q):

  area=(p*q)/2

  return area

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(p, q, expected):
    try:
        if validate_solution(rombus_area(
            p, q),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



