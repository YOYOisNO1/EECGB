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
# Write a function to insert an element before each element of a list.
#
# SOLUTION CODE
# ============================================
def insert_element(list,element):

 list = [v for elt in list for v in (element, elt)]

 return list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list, element, expected):
    try:
        if validate_solution(insert_element(
            list, element),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



