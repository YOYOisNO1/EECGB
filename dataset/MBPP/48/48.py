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
# Write a python function to set all odd bits of a given number.
#
# SOLUTION CODE
# ============================================
def odd_bit_set_number(n):

    count = 0;res = 0;temp = n

    while temp > 0:

        if count % 2 == 0:

            res |= (1 << count)

        count += 1

        temp >>= 1

    return (n | res)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(odd_bit_set_number(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



