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
# Write a function to solve the fibonacci sequence using recursion.
#
# SOLUTION CODE
# ============================================
def fibonacci(n):

  if n == 1 or n == 2:

    return 1

  else:

    return (fibonacci(n - 1) + (fibonacci(n - 2)))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(fibonacci(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



