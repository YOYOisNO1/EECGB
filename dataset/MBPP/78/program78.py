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
# Write a python function to find number of integers with odd number of set bits.
#
# SOLUTION CODE
# ============================================
def count_with_odd_set_bits(n): 

    if (n % 2 != 0): 

        return (n + 1) / 2

    count = bin(n).count('1') 

    ans = n / 2

    if (count % 2 != 0): 

        ans += 1

    return ans 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(count_with_odd_set_bits(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



