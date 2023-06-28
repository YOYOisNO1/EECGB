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
# Write a python function to find minimum adjacent swaps required to sort binary array.
#
# SOLUTION CODE
# ============================================
def find_min_swaps(arr,n) : 

    noOfZeroes = [0] * n 

    count = 0 

    noOfZeroes[n - 1] = 1 - arr[n - 1] 

    for i in range(n-2,-1,-1) : 

        noOfZeroes[i] = noOfZeroes[i + 1] 

        if (arr[i] == 0) : 

            noOfZeroes[i] = noOfZeroes[i] + 1

    for i in range(0,n) : 

        if (arr[i] == 1) : 

            count = count + noOfZeroes[i] 

    return count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(find_min_swaps(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



