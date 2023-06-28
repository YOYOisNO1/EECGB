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
# Write a python function to split a string into characters.
#
# SOLUTION CODE
# ============================================
def split(word): 

    return [char for char in word] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(word, expected):
    try:
        if validate_solution(split(
            word),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



