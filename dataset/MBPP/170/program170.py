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
# Write a function to find sum of the numbers in a list between the indices of a specified range.
#
# SOLUTION CODE
# ============================================
def sum_range_list(list1, m, n):                                                                                                                                                                                                

    sum_range = 0                                                                                                                                                                                                         

    for i in range(m, n+1, 1):                                                                                                                                                                                        

        sum_range += list1[i]                                                                                                                                                                                                  

    return sum_range   

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, m, n, expected):
    try:
        if validate_solution(sum_range_list(
            list1, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



