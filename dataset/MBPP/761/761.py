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
# Write a function to caluclate arc length of an angle.
#
# SOLUTION CODE
# ============================================
def arc_length(d,a):

    pi=22/7

    if a >= 360:

        return None

    arclength = (pi*d) * (a/360)

    return arclength

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(d, a, expected):
    try:
        if validate_solution(arc_length(
            d, a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



