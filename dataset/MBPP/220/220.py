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
# Write a function to replace maximum n occurrences of spaces, commas, or dots with a colon.
#
# SOLUTION CODE
# ============================================
import re

def replace_max_specialchar(text,n):

 return (re.sub("[ ,.]", ":", text, n))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, n, expected):
    try:
        if validate_solution(replace_max_specialchar(
            text, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



