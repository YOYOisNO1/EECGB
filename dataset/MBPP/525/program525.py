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
# Write a python function to check whether two given lines are parallel or not.
#
# SOLUTION CODE
# ============================================
def parallel_lines(line1, line2):

  return line1[0]/line1[1] == line2[0]/line2[1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(line1, line2, expected):
    try:
        if validate_solution(parallel_lines(
            line1, line2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



