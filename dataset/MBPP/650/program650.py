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
# Write a python function to check whether the given two arrays are equal or not.
#
# SOLUTION CODE
# ============================================
def are_equal(arr1,arr2,n,m):

    if (n != m):

        return False

    arr1.sort()

    arr2.sort()

    for i in range(0,n - 1):

        if (arr1[i] != arr2[i]):

            return False

    return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr1, arr2, n, m, expected):
    try:
        if validate_solution(are_equal(
            arr1, arr2, n, m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



