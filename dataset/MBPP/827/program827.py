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
# Write a function to sum a specific column of a list in a given list of lists.
#
# SOLUTION CODE
# ============================================
def sum_column(list1, C):

    result = sum(row[C] for row in list1)

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, c, expected):
    try:
        if validate_solution(sum_column(
            list1, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



