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
# Write a python function to count occurences of a character in a repeated string.
#
# SOLUTION CODE
# ============================================
def count_char(str,x): 

    count = 0

    for i in range(len(str)):  

        if (str[i] == x) : 

            count += 1

    n = 10

    repititions = n // len(str)  

    count = count * repititions  

    l = n % len(str)  

    for i in range(l): 

        if (str[i] == x):  

            count += 1

    return count  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, x, expected):
    try:
        if validate_solution(count_char(
            str, x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



