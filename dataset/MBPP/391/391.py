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
# Write a function to convert more than one list to nested dictionary.
#
# SOLUTION CODE
# ============================================
def convert_list_dictionary(l1, l2, l3):

     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]

     return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l1, l2, l3, expected):
    try:
        if validate_solution(convert_list_dictionary(
            l1, l2, l3),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



