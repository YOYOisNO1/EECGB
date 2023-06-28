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
# Write a python function to count the occcurences of an element in a tuple.
#
# SOLUTION CODE
# ============================================
def count_x(tup, x): 

    count = 0

    for ele in tup: 

        if (ele == x): 

            count = count + 1

    return count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(tup, x, expected):
    try:
        if validate_solution(count_x(
            tup, x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



