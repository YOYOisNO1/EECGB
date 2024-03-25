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
# Write a python function to check whether the two given strings are isomorphic to each other or not.
#
# SOLUTION CODE
# ============================================
def is_isomorphic(str1,str2):          

    dict_str1 = {}

    dict_str2 = {}

    for i, value in enumerate(str1):

        dict_str1[value] = dict_str1.get(value,[]) + [i]        

    for j, value in enumerate(str2):

        dict_str2[value] = dict_str2.get(value,[]) + [j]

    if sorted(dict_str1.values()) == sorted(dict_str2.values()):

        return True

    else:

        return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, str2, expected):
    try:
        if validate_solution(is_isomorphic(
            str1, str2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



