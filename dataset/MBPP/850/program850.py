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
# Write a function to check if a triangle of positive area is possible with the given angles.
#
# SOLUTION CODE
# ============================================
def is_triangleexists(a,b,c): 

    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180): 

        if((a + b)>= c or (b + c)>= a or (a + c)>= b): 

            return True 

        else:

            return False

    else:

        return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, c, expected):
    try:
        if validate_solution(is_triangleexists(
            a, b, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



