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
# Write a function to find the difference of first even and odd number of a given list.
#
# SOLUTION CODE
# ============================================
def diff_even_odd(list1):

    first_even = next((el for el in list1 if el%2==0),-1)

    first_odd = next((el for el in list1 if el%2!=0),-1)

    return (first_even-first_odd)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(diff_even_odd(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



