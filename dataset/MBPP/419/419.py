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
# Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
#
# SOLUTION CODE
# ============================================
def round_and_sum(list1):

  lenght=len(list1)

  round_and_sum=sum(list(map(round,list1))* lenght)

  return round_and_sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(round_and_sum(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



