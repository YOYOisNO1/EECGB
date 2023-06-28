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
# Write a python function to find the sum of xor of all pairs of numbers in the given array.
#
# SOLUTION CODE
# ============================================
def pair_or_sum(arr,n) : 

    ans = 0 

    for i in range(0,n) :    

        for j in range(i + 1,n) :   

            ans = ans + (arr[i] ^ arr[j])          

    return ans 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(pair_or_sum(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



