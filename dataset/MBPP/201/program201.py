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
# Write a python function to check whether the elements in a list are same or not.
#
# SOLUTION CODE
# ============================================
def chk_list(lst): 

    return len(set(lst)) == 1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(lst, expected):
    try:
        if validate_solution(chk_list(
            lst),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



