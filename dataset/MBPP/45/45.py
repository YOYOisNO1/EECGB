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
# Write a function to find the gcd of the given array elements.
#
# SOLUTION CODE
# ============================================
def find_gcd(x, y): 

	while(y): 

		x, y = y, x % y 

	return x 

def get_gcd(l):

  num1 = l[0]

  num2 = l[1]

  gcd = find_gcd(num1, num2)

  for i in range(2, len(l)):

    gcd = find_gcd(gcd, l[i])

  return gcd

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, expected):
    try:
        if validate_solution(find_gcd(
            l),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



