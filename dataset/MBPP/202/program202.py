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
# Write a function to remove even characters in a string.
#
# SOLUTION CODE
# ============================================
def remove_even(str1):

 str2 = ''

 for i in range(1, len(str1) + 1):

    if(i % 2 != 0):

        str2 = str2 + str1[i - 1]

 return str2

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(remove_even(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



