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
# Write a function to calculate the standard deviation.
#
# SOLUTION CODE
# ============================================
import math

import sys

def sd_calc(data):

    n = len(data)

    if n <= 1:

        return 0.0

    mean, sd = avg_calc(data), 0.0

    for el in data:

        sd += (float(el) - mean)**2

    sd = math.sqrt(sd / float(n-1))

    return sd

def avg_calc(ls):

    n, mean = len(ls), 0.0

    if n <= 1:

        return ls[0]

    for el in ls:

        mean = mean + float(el)

    mean = mean / float(n)

    return mean

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(data_arg0, expected):
    try:
        if validate_solution(sd_calc(
            data_arg0),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



