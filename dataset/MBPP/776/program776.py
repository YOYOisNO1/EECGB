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
# Write a function to count those characters which have vowels as their neighbors in the given string.
#
# SOLUTION CODE
# ============================================
def count_vowels(test_str):

  res = 0

  vow_list = ['a', 'e', 'i', 'o', 'u']

  for idx in range(1, len(test_str) - 1):

    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):

      res += 1

  if test_str[0] not in vow_list and test_str[1] in vow_list:

    res += 1

  if test_str[-1] not in vow_list and test_str[-2] in vow_list:

    res += 1

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_str, expected):
    try:
        if validate_solution(count_vowels(
            test_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



