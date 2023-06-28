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
# Write a python function to check if a given number is one less than twice its reverse.
#
# SOLUTION CODE
# ============================================
def rev(num):    

    rev_num = 0

    while (num > 0):  

        rev_num = (rev_num * 10 + num % 10) 

        num = num // 10  

    return rev_num  

def check(n):    

    return (2 * rev(n) == n + 1)  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(rev(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



