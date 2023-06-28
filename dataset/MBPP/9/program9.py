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
# Write a python function to find the minimum number of rotations required to get the same string.
#
# SOLUTION CODE
# ============================================
def find_rotations(str): 

    tmp = str + str

    n = len(str) 

    for i in range(1,n + 1): 

        substring = tmp[i: i+n] 

        if (str == substring): 

            return i 

    return n 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(find_rotations(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



