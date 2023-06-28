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
# Write a function to join the tuples if they have similar initial elements.
#
# SOLUTION CODE
# ============================================
def join_tuples(test_list):

  res = []

  for sub in test_list:

    if res and res[-1][0] == sub[0]:

      res[-1].extend(sub[1:])

    else:

      res.append([ele for ele in sub])

  res = list(map(tuple, res))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(join_tuples(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



