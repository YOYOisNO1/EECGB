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
# Write a function to sort the given tuple list basis the total digits in tuple.
#
# SOLUTION CODE
# ============================================
def count_digs(tup):

  return sum([len(str(ele)) for ele in tup ]) 

def sort_list(test_list):

  test_list.sort(key = count_digs)

  return (str(test_list))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(count_digs(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



