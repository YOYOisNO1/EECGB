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
# Write a function to find the lcm of the given array elements.
#
# SOLUTION CODE
# ============================================
def find_lcm(num1, num2): 

	if(num1>num2): 

		num = num1 

		den = num2 

	else: 

		num = num2 

		den = num1 

	rem = num % den 

	while (rem != 0): 

		num = den 

		den = rem 

		rem = num % den 

	gcd = den 

	lcm = int(int(num1 * num2)/int(gcd)) 

	return lcm 

def get_lcm(l):

  num1 = l[0]

  num2 = l[1]

  lcm = find_lcm(num1, num2)

  for i in range(2, len(l)):

    lcm = find_lcm(lcm, l[i])

  return lcm 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, expected):
    try:
        if validate_solution(find_lcm(
            l),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



