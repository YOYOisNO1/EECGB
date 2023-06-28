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
# Write a function to get the n largest items from a dataset.
#
# SOLUTION CODE
# ============================================
import heapq

def larg_nnum(list1,n):

 largest=heapq.nlargest(n,list1)

 return largest

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, n, expected):
    try:
        if validate_solution(larg_nnum(
            list1, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



