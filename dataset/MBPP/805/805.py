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
# Write a function to find the list in a list of lists whose sum of elements is the highest.
#
# SOLUTION CODE
# ============================================
def max_sum_list(lists):

 return max(lists, key=sum)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(lists, expected):
    try:
        if validate_solution(max_sum_list(
            lists),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



