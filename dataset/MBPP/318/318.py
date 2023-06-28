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
# Write a python function to find the maximum volume of a cuboid with given sum of sides.
#
# SOLUTION CODE
# ============================================
def max_volume (s): 

    maxvalue = 0

    i = 1

    for i in range(s - 1): 

        j = 1

        for j in range(s): 

            k = s - i - j 

            maxvalue = max(maxvalue, i * j * k)         

    return maxvalue 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution((
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



