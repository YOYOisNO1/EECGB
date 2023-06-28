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
# Write a python function to count unequal element pairs from the given array.
#
# SOLUTION CODE
# ============================================
def count_pairs(arr,n): 

    cnt = 0; 

    for i in range(n): 

        for j in range(i + 1,n): 

            if (arr[i] != arr[j]): 

                cnt += 1; 

    return cnt; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(count_pairs(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



