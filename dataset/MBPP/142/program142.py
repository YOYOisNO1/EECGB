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
# Write a function to count the same pair in three given lists.
#
# SOLUTION CODE
# ============================================
def count_samepair(list1,list2,list3):

    result = sum(m == n == o for m, n, o in zip(list1,list2,list3))

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, list2, list3, expected):
    try:
        if validate_solution(count_samepair(
            list1, list2, list3),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



