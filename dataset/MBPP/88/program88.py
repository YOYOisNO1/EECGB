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
# Write a function to get the frequency of the elements in a list.
#
# SOLUTION CODE
# ============================================
import collections

def freq_count(list1):

  freq_count= collections.Counter(list1)

  return freq_count

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(freq_count(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



