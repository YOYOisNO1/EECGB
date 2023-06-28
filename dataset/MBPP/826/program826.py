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
# Write a python function to find the type of triangle from the given sides.
#
# SOLUTION CODE
# ============================================
def check_type_of_triangle(a,b,c): 

    sqa = pow(a,2) 

    sqb = pow(b,2) 

    sqc = pow(c,2) 

    if (sqa == sqa + sqb or sqb == sqa + sqc or sqc == sqa + sqb): 

        return ("Right-angled Triangle") 

    elif (sqa > sqc + sqb or sqb > sqa + sqc or sqc > sqa + sqb): 

        return ("Obtuse-angled Triangle") 

    else: 

        return ("Acute-angled Triangle") 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, c, expected):
    try:
        if validate_solution(check_type_of_triangle(
            a, b, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



