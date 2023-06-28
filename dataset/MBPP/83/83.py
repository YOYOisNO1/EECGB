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
# Write a python function to find the character made by adding all the characters of the given string.
#
# SOLUTION CODE
# ============================================
def get_char(strr):  

    summ = 0

    for i in range(len(strr)): 

        summ += (ord(strr[i]) - ord('a') + 1)  

    if (summ % 26 == 0): 

        return ord('z') 

    else: 

        summ = summ % 26

        return chr(ord('a') + summ - 1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(strr, expected):
    try:
        if validate_solution(get_char(
            strr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



