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
# Write a python function to find the average of even numbers till a given even number.
#
# SOLUTION CODE
# ============================================
def average_even(n) : 

    if (n% 2!= 0) : 

        return ("Invalid Input") 

        return -1  

    sm = 0

    count = 0

    while (n>= 2) : 

        count = count+1

        sm = sm+n 

        n = n-2

    return sm // count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(average_even(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



