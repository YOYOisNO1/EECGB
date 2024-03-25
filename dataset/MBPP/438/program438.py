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
# Write a function to count bidirectional tuple pairs.
#
# SOLUTION CODE
# ============================================
def count_bidirectional(test_list):

  res = 0

  for idx in range(0, len(test_list)):

    for iidx in range(idx + 1, len(test_list)):

      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:

        res += 1

  return (str(res)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(count_bidirectional(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



