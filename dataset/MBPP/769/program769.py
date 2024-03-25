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
# Write a python function to get the difference between two lists.
#
# SOLUTION CODE
# ============================================
def diff(li1,li2):

    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(li1, li2, expected):
    try:
        if validate_solution(diff(
            li1, li2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



