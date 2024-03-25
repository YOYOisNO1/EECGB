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
# Write a function to remove all the words with k length in the given string.
#
# SOLUTION CODE
# ============================================
def remove_length(test_str, K):

  temp = test_str.split()

  res = [ele for ele in temp if len(ele) != K]

  res = ' '.join(res)

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_str, k, expected):
    try:
        if validate_solution(remove_length(
            test_str, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



