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
# Write a function for nth catalan number.
#
# SOLUTION CODE
# ============================================
def catalan_number(num):

    if num <=1:

         return 1   

    res_num = 0

    for i in range(num):

        res_num += catalan_number(i) * catalan_number(num-i-1)

    return res_num

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num, expected):
    try:
        if validate_solution(catalan_number(
            num),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



