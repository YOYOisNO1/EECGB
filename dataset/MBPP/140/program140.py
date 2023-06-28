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
# Write a function to extract elements that occur singly in the given tuple list.
#
# SOLUTION CODE
# ============================================
def extract_singly(test_list):

  res = []

  temp = set()

  for inner in test_list:

    for ele in inner:

      if not ele in temp:

        temp.add(ele)

        res.append(ele)

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(extract_singly(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



