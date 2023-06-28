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
# Write a function to check that the given string contains only a certain set of characters(in this case a-z, a-z and 0-9) by using regex.
#
# SOLUTION CODE
# ============================================
import re

def is_allowed_specific_char(string):

    get_char = re.compile(r'[^a-zA-Z0-9.]')

    string = get_char.search(string)

    return not bool(string)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, expected):
    try:
        if validate_solution(is_allowed_specific_char(
            string_arg0),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



