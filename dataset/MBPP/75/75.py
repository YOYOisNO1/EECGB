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
# Write a function to find tuples which have all elements divisible by k from the given list of tuples.
#
# SOLUTION CODE
# ============================================
def find_tuples(test_list, K):

  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]

  return (str(res)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, k, expected):
    try:
        if validate_solution(find_tuples(
            test_list, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



