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
# Write a python function to find the most significant bit number which is also a set bit.
#
# SOLUTION CODE
# ============================================
def set_bit_number(n): 

    if (n == 0): 

        return 0; 

    msb = 0; 

    n = int(n / 2); 

    while (n > 0): 

        n = int(n / 2); 

        msb += 1; 

    return (1 << msb)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(set_bit_number(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



