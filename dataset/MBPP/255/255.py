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
# Write a function to choose specified number of colours from three different colours and generate all the combinations with repetitions.
#
# SOLUTION CODE
# ============================================
from itertools import combinations_with_replacement 

def combinations_colors(l, n):

    return list(combinations_with_replacement(l,n))


# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, n, expected):
    try:
        if validate_solution(combinations_colors(
            l, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



