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
# Write a function to find area of a sector.
#
# SOLUTION CODE
# ============================================
def sector_area(r,a):

    pi=22/7

    if a >= 360:

        return None

    sectorarea = (pi*r**2) * (a/360)

    return sectorarea

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(r, a, expected):
    try:
        if validate_solution(sector_area(
            r, a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



