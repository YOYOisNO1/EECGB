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
# Write a function to check whether the given number is armstrong or not.
#
# SOLUTION CODE
# ============================================
def armstrong_number(number):

 sum = 0

 times = 0

 temp = number

 while temp > 0:

           times = times + 1

           temp = temp // 10

 temp = number

 while temp > 0:

           reminder = temp % 10

           sum = sum + (reminder ** times)

           temp //= 10

 if number == sum:

           return True

 else:

           return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(number, expected):
    try:
        if validate_solution(armstrong_number(
            number),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



