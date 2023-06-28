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
# Write a python function to find nth number in a sequence which is not a multiple of a given number.
#
# SOLUTION CODE
# ============================================
def count_no (A,N,L,R): 

    count = 0

    for i in range (L,R + 1): 

        if (i % A != 0): 

            count += 1

        if (count == N): 

            break

    return (i) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, l, r, expected):
    try:
        if validate_solution((
            a, n, l, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



