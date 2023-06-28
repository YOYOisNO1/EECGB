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
# Write a function to split a string at lowercase letters.
#
# SOLUTION CODE
# ============================================
import re

def split_lowerstring(text):

 return (re.findall('[a-z][^a-z]*', text))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, expected):
    try:
        if validate_solution(split_lowerstring(
            text),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



