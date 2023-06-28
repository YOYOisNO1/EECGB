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
# Write a function to iterate over elements repeating each as many times as its count.
#
# SOLUTION CODE
# ============================================
from collections import Counter

def count_variable(a,b,c,d):

  c = Counter(p=a, q=b, r=c, s=d)

  return list(c.elements())

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, c, d, expected):
    try:
        if validate_solution(count_variable(
            a, b, c, d),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



