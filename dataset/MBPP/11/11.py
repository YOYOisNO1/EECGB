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
# Write a python function to remove first and last occurrence of a given character from the string.
#
# SOLUTION CODE
# ============================================
def remove_occ(s,ch): 

    for i in range(len(s)): 

        if (s[i] == ch): 

            s = s[0 : i] + s[i + 1:] 

            break

    for i in range(len(s) - 1,-1,-1):  

        if (s[i] == ch): 

            s = s[0 : i] + s[i + 1:] 

            break

    return s 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, ch, expected):
    try:
        if validate_solution(remove_occ(
            s, ch),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



