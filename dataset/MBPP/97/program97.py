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
# Write a function to find frequency count of list of lists.
#
# SOLUTION CODE
# ============================================
def frequency_lists(list1):

    list1 = [item for sublist in list1 for item in sublist]

    dic_data = {}

    for num in list1:

        if num in dic_data.keys():

            dic_data[num] += 1

        else:

            key = num

            value = 1

            dic_data[key] = value

    return dic_data



# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(frequency_lists(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



