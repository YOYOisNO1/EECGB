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
# Write a function to create a list containing the power of said number in bases raised to the corresponding number in the index using map function.
#
# SOLUTION CODE
# ============================================
def basesnum_coresspondingnum(bases_num,index):

  result = list(map(pow, bases_num, index))

  return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(bases_num, index, expected):
    try:
        if validate_solution(basesnum_coresspondingnum(
            bases_num, index),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



