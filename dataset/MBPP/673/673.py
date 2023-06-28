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
# Write a python function to convert a list of multiple integers into a single integer.
#
# SOLUTION CODE
# ============================================
def convert(list): 

    s = [str(i) for i in list] 

    res = int("".join(s))  

    return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list, expected):
    try:
        if validate_solution(convert(
            list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



