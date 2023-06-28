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
# Write a python function to check whether the hexadecimal number is even or odd.
#
# SOLUTION CODE
# ============================================
def even_or_odd(N): 

    l = len(N) 

    if (N[l-1] =='0'or N[l-1] =='2'or 

        N[l-1] =='4'or N[l-1] =='6'or 

        N[l-1] =='8'or N[l-1] =='A'or 

        N[l-1] =='C'or N[l-1] =='E'): 

        return ("Even") 

    else: 

        return ("Odd") 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(even_or_odd(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



