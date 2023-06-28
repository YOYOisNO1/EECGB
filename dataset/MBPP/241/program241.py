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
# Write a function to generate a 3d array having each element as '*'.
#
# SOLUTION CODE
# ============================================
def array_3d(m,n,o):

 array_3d = [[ ['*' for col in range(m)] for col in range(n)] for row in range(o)]

 return array_3d

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(m, n, o, expected):
    try:
        if validate_solution(array_3d(
            m, n, o),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



