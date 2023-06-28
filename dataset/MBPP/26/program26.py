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
# Write a function to check if the given tuple list has all k elements.
#
# SOLUTION CODE
# ============================================
def check_k_elements(test_list, K):

  res = True

  for tup in test_list:

    for ele in tup:

      if ele != K:

        res = False

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, k, expected):
    try:
        if validate_solution(check_k_elements(
            test_list, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



