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
# Write a python function to remove negative numbers from a list.
#
# SOLUTION CODE
# ============================================
def remove_negs(num_list): 

    for item in num_list: 

        if item < 0: 

           num_list.remove(item) 

    return num_list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num_list, expected):
    try:
        if validate_solution(remove_negs(
            num_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



