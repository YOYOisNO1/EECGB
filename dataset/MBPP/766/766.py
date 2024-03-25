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
# Write a function to iterate over all pairs of consecutive items in a given list.
#
# SOLUTION CODE
# ============================================
def pair_wise(l1):

    temp = []

    for i in range(len(l1) - 1):

        current_element, next_element = l1[i], l1[i + 1]

        x = (current_element, next_element)

        temp.append(x)

    return temp

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l1, expected):
    try:
        if validate_solution(pair_wise(
            l1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



