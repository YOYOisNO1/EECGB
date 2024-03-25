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
# Write a python function to count the number of lists in a given number of lists.
#
# SOLUTION CODE
# ============================================
def count_list(input_list): 

    return len(input_list)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(input_list, expected):
    try:
        if validate_solution(count_list(
            input_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



