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
# Write a python function to count the number of rectangles in a circle of radius r.
#
# SOLUTION CODE
# ============================================
def count_rectangles(radius):  

    rectangles = 0 

    diameter = 2 * radius 

    diameterSquare = diameter * diameter 

    for a in range(1, 2 * radius):  

        for b in range(1, 2 * radius): 

            diagnalLengthSquare = (a * a +  b * b)  

            if (diagnalLengthSquare <= diameterSquare) : 

                rectangles += 1

    return rectangles 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(radius, expected):
    try:
        if validate_solution(count_rectangles(
            radius),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



