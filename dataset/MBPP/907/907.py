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
# Write a function to print the first n lucky numbers.
#
# SOLUTION CODE
# ============================================
def lucky_num(n):

 List=range(-1,n*n+9,2)

 i=2

 while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1

 return List[1:n+1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(lucky_num(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



