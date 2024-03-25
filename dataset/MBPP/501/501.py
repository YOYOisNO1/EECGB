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
# Write a python function to find common divisor between two numbers in a given pair.
#
# SOLUTION CODE
# ============================================
def ngcd(x,y):

    i=1

    while(i<=x and i<=y):

        if(x%i==0 and y%i == 0):

            gcd=i;

        i+=1

    return gcd;

def num_comm_div(x,y):

  n = ngcd(x,y)

  result = 0

  z = int(n**0.5)

  i = 1

  while(i <= z):

    if(n % i == 0):

      result += 2 

      if(i == n/i):

        result-=1

    i+=1

  return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, expected):
    try:
        if validate_solution(ngcd(
            x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



