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
# Write a python function to find the first repeated word in a given string.
#
# SOLUTION CODE
# ============================================
def first_repeated_word(str1):

  temp = set()

  for word in str1.split():

    if word in temp:

      return word;

    else:

      temp.add(word)

  return 'None'

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(first_repeated_word(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



