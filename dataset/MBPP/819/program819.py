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
# Write a function to count the frequency of consecutive duplicate elements in a given list of numbers.
#
# SOLUTION CODE
# ============================================
def count_duplic(lists):

    element = []

    frequency = []

    if not lists:

        return element

    running_count = 1

    for i in range(len(lists)-1):

        if lists[i] == lists[i+1]:

            running_count += 1

        else:

            frequency.append(running_count)

            element.append(lists[i])

            running_count = 1

    frequency.append(running_count)

    element.append(lists[i+1])

    return element,frequency



# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(lists, expected):
    try:
        if validate_solution(count_duplic(
            lists),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



