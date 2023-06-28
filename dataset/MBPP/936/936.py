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
# Write a function to re-arrange the given tuples based on the given ordered list.
#
# SOLUTION CODE
# ============================================
def re_arrange_tuples(test_list, ord_list):

  temp = dict(test_list)

  res = [(key, temp[key]) for key in ord_list]

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, ord_list, expected):
    try:
        if validate_solution(re_arrange_tuples(
            test_list, ord_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



