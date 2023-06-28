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
# Write a function to reverse strings in a given list of string values.
#
# SOLUTION CODE
# ============================================
def reverse_string_list(stringlist):

    result = [x[::-1] for x in stringlist]

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(stringlist, expected):
    try:
        if validate_solution(reverse_string_list(
            stringlist),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



