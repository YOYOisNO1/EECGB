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
# Write a function to put spaces between words starting with capital letters in a given string by using regex.
#
# SOLUTION CODE
# ============================================
import re

def capital_words_spaces(str1):

  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(capital_words_spaces(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



