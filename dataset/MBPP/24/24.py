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
# Write a function to convert the given binary number to its decimal equivalent.
#
# SOLUTION CODE
# ============================================
def binary_to_decimal(binary): 

    binary1 = binary 

    decimal, i, n = 0, 0, 0

    while(binary != 0): 

        dec = binary % 10

        decimal = decimal + dec * pow(2, i) 

        binary = binary//10

        i += 1

    return (decimal)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(binary, expected):
    try:
        if validate_solution(binary_to_decimal(
            binary),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



