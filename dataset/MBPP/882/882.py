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
# Write a function to caluclate perimeter of a parallelogram.
#
# SOLUTION CODE
# ============================================
def parallelogram_perimeter(b,h):

  perimeter=2*(b*h)

  return perimeter

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(b, h, expected):
    try:
        if validate_solution(parallelogram_perimeter(
            b, h),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



