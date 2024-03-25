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
# Write a function to calculate volume of a tetrahedron.
#
# SOLUTION CODE
# ============================================
import math

def volume_tetrahedron(num):

	volume = (num ** 3 / (6 * math.sqrt(2)))	

	return round(volume, 2)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(num, expected):
    try:
        if validate_solution(volume_tetrahedron(
            num),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



