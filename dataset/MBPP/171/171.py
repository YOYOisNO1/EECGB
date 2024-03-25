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
# Write a function to find the perimeter of a pentagon.
#
# SOLUTION CODE
# ============================================
import math

def perimeter_pentagon(a):

  perimeter=(5*a)

  return perimeter

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, expected):
    try:
        if validate_solution(perimeter_pentagon(
            a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



