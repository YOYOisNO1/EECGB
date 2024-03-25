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
# Write a function to sort the given array by using merge sort.
#
# SOLUTION CODE
# ============================================
def merge(a,b):

    c = []

    while len(a) != 0 and len(b) != 0:

        if a[0] < b[0]:

            c.append(a[0])

            a.remove(a[0])

        else:

            c.append(b[0])

            b.remove(b[0])

    if len(a) == 0:

        c += b

    else:

        c += a

    return c

def merge_sort(x):

    if len(x) == 0 or len(x) == 1:

        return x

    else:

        middle = len(x)//2

        a = merge_sort(x[:middle])

        b = merge_sort(x[middle:])

        return merge(a,b)



# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, expected):
    try:
        if validate_solution(merge(
            x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



