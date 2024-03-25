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
# Write a python function to find nth bell number.
#
# SOLUTION CODE
# ============================================
def bell_number(n): 

    bell = [[0 for i in range(n+1)] for j in range(n+1)] 

    bell[0][0] = 1

    for i in range(1, n+1):

        bell[i][0] = bell[i-1][i-1]

        for j in range(1, i+1): 

            bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 

    return bell[n][0] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(bell_number(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



