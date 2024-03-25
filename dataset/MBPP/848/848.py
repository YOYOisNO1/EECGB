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
# Write a function to find the area of a trapezium.
#
# SOLUTION CODE
# ============================================
def area_trapezium(base1,base2,height):

 area = 0.5 * (base1 + base2) * height

 return area

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(base1, base2, height, expected):
    try:
        if validate_solution(area_trapezium(
            base1, base2, height),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



