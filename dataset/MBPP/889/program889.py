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
# Write a function to reverse each list in a given list of lists.
#
# SOLUTION CODE
# ============================================
def reverse_list_lists(lists):

    for l in lists:

        l.sort(reverse = True)

    return lists 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(lists, expected):
    try:
        if validate_solution(reverse_list_lists(
            lists),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



