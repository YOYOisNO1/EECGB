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
# Write a function to find the vertex of a parabola.
#
# SOLUTION CODE
# ============================================
def parabola_vertex(a, b, c): 

  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))

  return vertex

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, c, expected):
    try:
        if validate_solution(parabola_vertex(
            a, b, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



