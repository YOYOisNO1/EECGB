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
# Write a function to sort the given array by using heap sort.
#
# SOLUTION CODE
# ============================================
def heap_sort(arr):

    heapify(arr)  

    end = len(arr) - 1

    while end > 0:

        arr[end], arr[0] = arr[0], arr[end]

        shift_down(arr, 0, end - 1)

        end -= 1

    return arr



def heapify(arr):

    start = len(arr) // 2

    while start >= 0:

        shift_down(arr, start, len(arr) - 1)

        start -= 1

def shift_down(arr, start, end):

    root = start

    while root * 2 + 1 <= end:

        child = root * 2 + 1

        if child + 1 <= end and arr[child] < arr[child + 1]:

            child += 1

        if child <= end and arr[root] < arr[child]:

            arr[root], arr[child] = arr[child], arr[root]

            root = child

        else:

            return



# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, expected):
    try:
        if validate_solution(heap_sort(
            arr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



