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
# Write a function to check if the given integer is a prime number.
#
# SOLUTION CODE
# ============================================
def prime_num(num):

  if num >=1:

   for i in range(2, num//2):

     if (num % i) == 0:

                return False

     else:

                return True

  else:

          return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num, expected):
    try:
        if validate_solution(prime_num(
            num),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



