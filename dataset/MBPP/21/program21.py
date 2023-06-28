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
# Write a function to find m number of multiples of n.
#
# SOLUTION CODE
# ============================================
def multiples_of_num(m,n): 

    multiples_of_num= list(range(n,(m+1)*n, n)) 

    return list(multiples_of_num)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(m, n, expected):
    try:
        if validate_solution(multiples_of_num(
            m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



