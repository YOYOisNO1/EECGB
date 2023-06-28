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
# Write a function to search a literals string in a string and also find the location within the original string where the pattern occurs.
#
# SOLUTION CODE
# ============================================
import re

def search_literal(pattern,text):

 match = re.search(pattern, text)

 s = match.start()

 e = match.end()

 return (s, e)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(pattern, text, expected):
    try:
        if validate_solution(search_literal(
            pattern, text),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



