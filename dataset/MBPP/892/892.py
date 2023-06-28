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
# Write a function to remove multiple spaces in a string.
#
# SOLUTION CODE
# ============================================
import re

def remove_spaces(text):

 return (re.sub(' +',' ',text))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, expected):
    try:
        if validate_solution(remove_spaces(
            text),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



