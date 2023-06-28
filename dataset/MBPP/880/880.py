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
# Write a python function to find number of solutions in quadratic equation.
#
# SOLUTION CODE
# ============================================
def check_solution(a,b,c) : 

    if ((b*b) - (4*a*c)) > 0 : 

        return ("2 solutions") 

    elif ((b*b) - (4*a*c)) == 0 : 

        return ("1 solution") 

    else : 

        return ("No solutions") 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, c, expected):
    try:
        if validate_solution(check_solution(
            a, b, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



