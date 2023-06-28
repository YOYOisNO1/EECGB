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
# Write a python function to check whether the given two integers have opposite sign or not.
#
# SOLUTION CODE
# ============================================
def opposite_signs(x,y): 

    return ((x ^ y) < 0); 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, expected):
    try:
        if validate_solution(opposite_signs(
            x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



