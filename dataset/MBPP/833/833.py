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
# Write a function to get dictionary keys as a list.
#
# SOLUTION CODE
# ============================================
def get_key(dict): 

    list = [] 

    for key in dict.keys(): 

        list.append(key)           

    return list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(dict, expected):
    try:
        if validate_solution(get_key(
            dict),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



