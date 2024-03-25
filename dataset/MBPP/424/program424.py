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
# Write a function to extract only the rear index element of each string in the given tuple.
#
# SOLUTION CODE
# ============================================
def extract_rear(test_tuple):

  res = list(sub[len(sub) - 1] for sub in test_tuple)

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tuple, expected):
    try:
        if validate_solution(extract_rear(
            test_tuple),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



