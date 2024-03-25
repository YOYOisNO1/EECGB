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
# Write a python function to check whether the given string is made up of two alternating characters or not.
#
# SOLUTION CODE
# ============================================
def is_two_alter(s):  

    for i in range (len( s) - 2) : 

        if (s[i] != s[i + 2]) : 

            return False

    if (s[0] == s[1]): 

        return False

    return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(is_two_alter(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



