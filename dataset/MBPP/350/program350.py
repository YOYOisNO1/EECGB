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
# Write a python function to minimize the length of the string by removing occurrence of only one character.
#
# SOLUTION CODE
# ============================================
def minimum_length(s) : 

    maxOcc = 0

    n = len(s) 

    arr = [0]*26

    for i in range(n) : 

        arr[ord(s[i]) -ord('a')] += 1

    for i in range(26) : 

        if arr[i] > maxOcc : 

            maxOcc = arr[i] 

    return n - maxOcc 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(minimum_length(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



