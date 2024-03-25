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
# Write a function to add two numbers and print number of digits of sum.
#
# SOLUTION CODE
# ============================================
def count_digits(num1,num2):

    number=num1+num2

    count = 0

    while(number > 0):

        number = number // 10

        count = count + 1

    return count

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num1, num2, expected):
    try:
        if validate_solution(count_digits(
            num1, num2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



