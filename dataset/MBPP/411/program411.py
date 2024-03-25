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
# Write a function to convert the given snake case string to camel case string by using regex.
#
# SOLUTION CODE
# ============================================
import re

def snake_to_camel(word):

  return ''.join(x.capitalize() or '_' for x in word.split('_'))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(word, expected):
    try:
        if validate_solution(snake_to_camel(
            word),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



