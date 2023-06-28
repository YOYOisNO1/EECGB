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
# Write a function to group the 1st elements on the basis of 2nd elements in the given tuple list.
#
# SOLUTION CODE
# ============================================
from itertools import groupby 

def group_element(test_list):

  res = dict()

  for key, val in groupby(sorted(test_list, key = lambda ele: ele[1]), key = lambda ele: ele[1]):

    res[key] = [ele[0] for ele in val] 

  return (res)



# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(group_element(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



