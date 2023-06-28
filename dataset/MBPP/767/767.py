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
# Write a python function to count the number of pairs whose sum is equal to sum.
#
# SOLUTION CODE
# ============================================
def get_pairs_count(arr,n,sum):

    count = 0  

    for i in range(0,n):

        for j in range(i + 1,n):

            if arr[i] + arr[j] == sum:

                count += 1

    return count

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, sum, expected):
    try:
        if validate_solution(get_pairs_count(
            arr, n, sum),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



