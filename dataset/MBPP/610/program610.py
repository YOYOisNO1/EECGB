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
# Write a python function to remove the k'th element from a given list.
#
# SOLUTION CODE
# ============================================
def remove_kth_element(list1, L):

    return  list1[:L-1] + list1[L:]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, l, expected):
    try:
        if validate_solution(remove_kth_element(
            list1, l),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



