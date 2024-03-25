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
# Write a function to find the minimum number of platforms required for a railway/bus station.
#
# SOLUTION CODE
# ============================================
def find_platform(arr, dep, n): 

    arr.sort() 

    dep.sort() 

    plat_needed = 1

    result = 1

    i = 1

    j = 0

    while (i < n and j < n): 

        if (arr[i] <= dep[j]):           

            plat_needed+= 1

            i+= 1

        elif (arr[i] > dep[j]):           

            plat_needed-= 1

            j+= 1

        if (plat_needed > result):  

            result = plat_needed           

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, dep, n, expected):
    try:
        if validate_solution(find_platform(
            arr, dep, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



