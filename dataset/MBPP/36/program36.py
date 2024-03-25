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
# Write a python function to find the nth digit in the proper fraction of two given numbers.
#
# SOLUTION CODE
# ============================================
def find_nth_digit(p,q,N) :  

    while (N > 0) : 

        N -= 1;  

        p *= 10;  

        res = p // q;  

        p %= q;  

    return res;  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(p, q, n, expected):
    try:
        if validate_solution(find_nth_digit(
            p, q, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



