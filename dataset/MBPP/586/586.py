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
# Write a python function to split the array and add the first part to the end.
#
# SOLUTION CODE
# ============================================
def split_arr(a,n,k):  

   b = a[:k] 

   return (a[k::]+b[::]) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, k, expected):
    try:
        if validate_solution(split_arr(
            a, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



