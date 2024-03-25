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
# Write a function to check if the two given strings are permutations of each other.
#
# SOLUTION CODE
# ============================================
def check_permutation(str1, str2):

  n1=len(str1)

  n2=len(str2)

  if(n1!=n2):

    return False

  a=sorted(str1)

  str1=" ".join(a)

  b=sorted(str2)

  str2=" ".join(b)

  for i in range(0, n1, 1):

    if(str1[i] != str2[i]):

      return False

  return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, str2, expected):
    try:
        if validate_solution(check_permutation(
            str1, str2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



