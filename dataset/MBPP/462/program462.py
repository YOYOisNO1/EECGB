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
# Write a function to find all possible combinations of the elements of a given list.
#
# SOLUTION CODE
# ============================================
def combinations_list(list1):

    if len(list1) == 0:

        return [[]]

    result = []

    for el in combinations_list(list1[1:]):

        result += [el, el+[list1[0]]]

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(combinations_list(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



