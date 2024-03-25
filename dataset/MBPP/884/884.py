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
# Write a python function to check whether all the bits are within a given range or not.
#
# SOLUTION CODE
# ============================================
def all_bits_set_in_the_given_range(n,l,r): 

    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1) 

    new_num = n & num 

    if (num == new_num): 

        return True

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, l, r, expected):
    try:
        if validate_solution(all_bits_set_in_the_given_range(
            n, l, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



