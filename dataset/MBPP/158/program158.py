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
# Write a python function to find k number of operations required to make all elements equal.
#
# SOLUTION CODE
# ============================================
def min_ops(arr,n,k): 

    max1 = max(arr) 

    res = 0

    for i in range(0,n):  

        if ((max1 - arr[i]) % k != 0): 

            return -1 

        else: 

            res += (max1 - arr[i]) / k 

    return int(res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, k, expected):
    try:
        if validate_solution(min_ops(
            arr, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



