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
# Write a function to extract unique values from the given dictionary values.
#
# SOLUTION CODE
# ============================================
def extract_unique(test_dict):

  res = list(sorted({ele for val in test_dict.values() for ele in val}))

  return res

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_dict, expected):
    try:
        if validate_solution(extract_unique(
            test_dict),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



