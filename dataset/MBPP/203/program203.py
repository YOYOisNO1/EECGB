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
# Write a python function to find the hamming distance between given two integers.
#
# SOLUTION CODE
# ============================================
def hamming_distance(n1,n2) : 

    x = n1 ^ n2  

    setBits = 0

    while (x > 0) : 

        setBits += x & 1

        x >>= 1

    return setBits  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n1, n2, expected):
    try:
        if validate_solution(hamming_distance(
            n1, n2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



