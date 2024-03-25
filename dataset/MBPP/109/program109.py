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
# Write a python function to find the count of rotations of a binary string with odd value.
#
# SOLUTION CODE
# ============================================
def odd_equivalent(s,n): 

    count=0

    for i in range(0,n): 

        if (s[i] == '1'): 

            count = count + 1

    return count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, n, expected):
    try:
        if validate_solution(odd_equivalent(
            s, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



