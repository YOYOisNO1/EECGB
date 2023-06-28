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
# Write a python function to convert octal number to decimal number.
#
# SOLUTION CODE
# ============================================
def octal_to_decimal(n):  

    num = n; 

    dec_value = 0; 

    base = 1; 

    temp = num; 

    while (temp): 

        last_digit = temp % 10; 

        temp = int(temp / 10); 

        dec_value += last_digit*base; 

        base = base * 8; 

    return dec_value; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(octal_to_decimal(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



