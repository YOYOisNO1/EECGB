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
# Write a function to find the item with maximum occurrences in a given list.
#
# SOLUTION CODE
# ============================================
def max_occurrences(list1):

    max_val = 0

    result = list1[0] 

    for i in list1:

        occu = list1.count(i)

        if occu > max_val:

            max_val = occu

            result = i 

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(max_occurrences(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



