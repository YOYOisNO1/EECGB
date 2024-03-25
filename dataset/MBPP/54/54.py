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
# Write a function to sort the given array by using counting sort.
#
# SOLUTION CODE
# ============================================
def counting_sort(my_list):

    max_value = 0

    for i in range(len(my_list)):

        if my_list[i] > max_value:

            max_value = my_list[i]

    buckets = [0] * (max_value + 1)

    for i in my_list:

        buckets[i] += 1

    i = 0

    for j in range(max_value + 1):

         for a in range(buckets[j]):

             my_list[i] = j

             i += 1

    return my_list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(my_list, expected):
    try:
        if validate_solution(counting_sort(
            my_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



