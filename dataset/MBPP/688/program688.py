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
# Write a function to get the length of a complex number.
#
# SOLUTION CODE
# ============================================
import cmath

def len_complex(a,b):

  cn=complex(a,b)

  length=abs(cn)

  return length

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(a, b, expected):
    try:
        if validate_solution(len_complex(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



