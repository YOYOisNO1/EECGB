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
# Write a python function to check if the string is a concatenation of another string.
#
# SOLUTION CODE
# ============================================
def check_concat(str1,str2):

    N = len(str1)

    M = len(str2)

    if (N % M != 0):

        return False

    for i in range(N):

        if (str1[i] != str2[i % M]):

            return False         

    return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, str2, expected):
    try:
        if validate_solution(check_concat(
            str1, str2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



