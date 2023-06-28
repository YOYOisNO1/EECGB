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
# Write a function to exchange the position of every n-th value with (n+1)th value and (n+1)th value with n-th value in a given list.
#
# SOLUTION CODE
# ============================================
from itertools import zip_longest, chain, tee

def exchange_elements(lst):

    lst1, lst2 = tee(iter(lst), 2)

    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(lst, expected):
    try:
        if validate_solution(exchange_elements(
            lst),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



