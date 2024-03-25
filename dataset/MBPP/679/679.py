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
# Write a function to access dictionary keys element by index.
#
# SOLUTION CODE
# ============================================
def access_key(ditionary,key):

  return list(ditionary)[key]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(ditionary, key, expected):
    try:
        if validate_solution(access_key(
            ditionary, key),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



