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
# Write a python function to find the maximum occurring character in a given string.
#
# SOLUTION CODE
# ============================================
def get_max_occuring_char(str1):

  ASCII_SIZE = 256

  ctr = [0] * ASCII_SIZE

  max = -1

  ch = ''

  for i in str1:

    ctr[ord(i)]+=1;

  for i in str1:

    if max < ctr[ord(i)]:

      max = ctr[ord(i)]

      ch = i

  return ch

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(get_max_occuring_char(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



