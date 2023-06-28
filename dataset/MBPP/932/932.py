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
# Write a function to remove duplicate words from a given list of strings.
#
# SOLUTION CODE
# ============================================
def remove_duplic_list(l):

    temp = []

    for x in l:

        if x not in temp:

            temp.append(x)

    return temp

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, expected):
    try:
        if validate_solution(remove_duplic_list(
            l),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



