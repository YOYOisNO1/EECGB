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
# Write a python function to convert a decimal number to binary number.
#
# SOLUTION CODE
# ============================================
def decimal_to_binary(N): 

    B_Number = 0

    cnt = 0

    while (N != 0): 

        rem = N % 2

        c = pow(10,cnt)  

        B_Number += rem*c  

        N //= 2 

        cnt += 1

    return B_Number  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(decimal_to_binary(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



