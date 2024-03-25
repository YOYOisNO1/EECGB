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
# Write a function to remove all elements from a given list present in another list.
#
# SOLUTION CODE
# ============================================
def remove_elements(list1, list2):

    result = [x for x in list1 if x not in list2]

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, list2, expected):
    try:
        if validate_solution(remove_elements(
            list1, list2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



