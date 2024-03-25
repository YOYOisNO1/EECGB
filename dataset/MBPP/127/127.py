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
# Write a function to multiply two integers without using the * operator in python.
#
# SOLUTION CODE
# ============================================
def multiply_int(x, y):

    if y < 0:

        return -multiply_int(x, -y)

    elif y == 0:

        return 0

    elif y == 1:

        return x

    else:

        return x + multiply_int(x, y - 1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, expected):
    try:
        if validate_solution(multiply_int(
            x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



