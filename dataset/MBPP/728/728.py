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
# Write a function to sum elements in two lists.
#
# SOLUTION CODE
# ============================================
def sum_list(lst1,lst2):

  res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 

  return res_list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(lst1, lst2, expected):
    try:
        if validate_solution(sum_list(
            lst1, lst2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



