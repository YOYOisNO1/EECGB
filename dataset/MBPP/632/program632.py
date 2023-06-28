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
# Write a python function to move all zeroes to the end of the given list.
#
# SOLUTION CODE
# ============================================
def move_zero(num_list):

    a = [0 for i in range(num_list.count(0))]

    x = [ i for i in num_list if i != 0]

    x.extend(a)

    return (x)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num_list, expected):
    try:
        if validate_solution(move_zero(
            num_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



