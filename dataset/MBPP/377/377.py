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
# Write a python function to remove all occurrences of a character in a given string.
#
# SOLUTION CODE
# ============================================
def remove_char(s,c) :  

    counts = s.count(c) 

    s = list(s) 

    while counts :  

        s.remove(c) 

        counts -= 1 

    s = '' . join(s)   

    return (s) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, c, expected):
    try:
        if validate_solution(remove_char(
            s, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



