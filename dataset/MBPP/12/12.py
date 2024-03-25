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
# Write a function to sort a given matrix in ascending order according to the sum of its rows.
#
# SOLUTION CODE
# ============================================
def sort_matrix(M):

    result = sorted(M, key=sum)

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(m, expected):
    try:
        if validate_solution(sort_matrix(
            m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



