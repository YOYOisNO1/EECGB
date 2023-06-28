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
# Write a function for computing square roots using the babylonian method.
#
# SOLUTION CODE
# ============================================
def babylonian_squareroot(number):

    if(number == 0):

        return 0;

    g = number/2.0;

    g2 = g + 1;

    while(g != g2):

        n = number/ g;

        g2 = g;

        g = (g + n)/2;

    return g;

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(number, expected):
    try:
        if validate_solution(babylonian_squareroot(
            number),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



