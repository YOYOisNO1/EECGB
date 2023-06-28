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
# Write a python function to toggle only first and last bits of a given number.
#
# SOLUTION CODE
# ============================================
def take_L_and_F_set_bits(n) : 

    n = n | n >> 1

    n = n | n >> 2

    n = n | n >> 4

    n = n | n >> 8

    n = n | n >> 16 

    return ((n + 1) >> 1) + 1      

def toggle_f_and_l_bits(n) :  

    if (n == 1) : 

        return 0 

    return n ^ take_L_and_F_set_bits(n) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(take_L_and_F_set_bits(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



