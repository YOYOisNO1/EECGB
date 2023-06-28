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
# Write a function to assign frequency to each tuple in the given tuple list.
#
# SOLUTION CODE
# ============================================
from collections import Counter 

def assign_freq(test_list):

  res = [(*key, val) for key, val in Counter(test_list).items()]

  return (str(res)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(assign_freq(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



