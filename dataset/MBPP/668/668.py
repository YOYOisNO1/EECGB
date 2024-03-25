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
# Write a python function to replace multiple occurence of character by single.
#
# SOLUTION CODE
# ============================================
import re 

def replace(string, char): 

    pattern = char + '{2,}'

    string = re.sub(pattern, char, string) 

    return string 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, char_arg1, expected):
    try:
        if validate_solution(replace(
            string_arg0, char_arg1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



