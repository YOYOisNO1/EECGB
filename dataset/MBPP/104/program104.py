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
# Write a function to sort each sublist of strings in a given list of lists using lambda function.
#
# SOLUTION CODE
# ============================================
def sort_sublists(input_list):

    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 

    return result


# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(input_list, expected):
    try:
        if validate_solution(sort_sublists(
            input_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



