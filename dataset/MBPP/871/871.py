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
# Write a python function to check whether the given strings are rotations of each other or not.
#
# SOLUTION CODE
# ============================================
def are_rotations(string1,string2): 

    size1 = len(string1) 

    size2 = len(string2) 

    temp = '' 

    if size1 != size2: 

        return False

    temp = string1 + string1 

    if (temp.count(string2)> 0): 

        return True

    else: 

        return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string1, string2, expected):
    try:
        if validate_solution(are_rotations(
            string1, string2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



