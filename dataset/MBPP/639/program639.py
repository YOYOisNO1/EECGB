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
# Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
#
# SOLUTION CODE
# ============================================
def sample_nam(sample_names):

  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))

  return len(''.join(sample_names))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(sample_names, expected):
    try:
        if validate_solution(sample_nam(
            sample_names),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



