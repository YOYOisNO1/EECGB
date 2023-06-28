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
# Write a function to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.
#
# SOLUTION CODE
# ============================================
def sum_difference(n):

    sumofsquares = 0

    squareofsum = 0

    for num in range(1, n+1):

        sumofsquares += num * num

        squareofsum += num

    squareofsum = squareofsum ** 2

    return squareofsum - sumofsquares

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(sum_difference(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



