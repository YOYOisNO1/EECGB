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
# Write a python function to find the largest number that can be formed with the given digits.
#
# SOLUTION CODE
# ============================================
def find_max_num(arr,n) : 

    arr.sort(reverse = True) 

    num = arr[0] 

    for i in range(1,n) : 

        num = num * 10 + arr[i] 

    return num 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(find_max_num(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



