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
# Write a function to find the second smallest number in a list.
#
# SOLUTION CODE
# ============================================
def second_smallest(numbers):

  if (len(numbers)<2):

    return

  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):

    return

  dup_items = set()

  uniq_items = []

  for x in numbers:

    if x not in dup_items:

      uniq_items.append(x)

      dup_items.add(x)

  uniq_items.sort()    

  return  uniq_items[1] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(numbers, expected):
    try:
        if validate_solution(second_smallest(
            numbers),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



