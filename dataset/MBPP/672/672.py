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
# Write a function to find maximum of three numbers.
#
# SOLUTION CODE
# ============================================
def max_of_three(num1,num2,num3): 

    if (num1 >= num2) and (num1 >= num3):

       lnum = num1

    elif (num2 >= num1) and (num2 >= num3):

       lnum = num2

    else:

       lnum = num3

    return lnum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num1, num2, num3, expected):
    try:
        if validate_solution(max_of_three(
            num1, num2, num3),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



