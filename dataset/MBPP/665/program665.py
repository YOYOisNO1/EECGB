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
# Write a python function to shift first element to the end of given list.
#
# SOLUTION CODE
# ============================================
def move_last(num_list):

    a = [num_list[0] for i in range(num_list.count(num_list[0]))]

    x = [ i for i in num_list if i != num_list[0]]

    x.extend(a)

    return (x)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num_list, expected):
    try:
        if validate_solution(move_last(
            num_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



