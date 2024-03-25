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
# Write a python function to check whether the given number can be represented by sum of two squares or not.
#
# SOLUTION CODE
# ============================================
def sum_square(n) : 

    i = 1 

    while i*i <= n : 

        j = 1

        while (j*j <= n) : 

            if (i*i+j*j == n) : 

                return True

            j = j+1

        i = i+1     

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(sum_square(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



