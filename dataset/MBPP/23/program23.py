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
# Write a python function to find the maximum sum of elements of list in a list of lists.
#
# SOLUTION CODE
# ============================================
def maximum_sum(list1): 

    maxi = -100000

    for x in list1: 

        sum = 0 

        for y in x: 

            sum+= y      

        maxi = max(sum,maxi)     

    return maxi 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(maximum_sum(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



