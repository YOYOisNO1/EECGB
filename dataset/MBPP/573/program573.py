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
# Write a python function to calculate the product of the unique numbers of a given list.
#
# SOLUTION CODE
# ============================================
def unique_product(list_data):

    temp = list(set(list_data))

    p = 1

    for i in temp:

        p *= i

    return p

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list_data, expected):
    try:
        if validate_solution(unique_product(
            list_data),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



