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
# Write a python function to find the largest postive number from the given list.
#
# SOLUTION CODE
# ============================================
def largest_pos(list1): 

    max = list1[0] 

    for x in list1: 

        if x > max : 

             max = x  

    return max

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(largest_pos(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



