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
# Write a python function to count the maximum number of equilateral triangles that can be formed within a given equilateral triangle.
#
# SOLUTION CODE
# ============================================
def no_of_triangle(N,K):

    if (N < K):

        return -1;

    else:

        Tri_up = 0;

        Tri_up = ((N - K + 1) *(N - K + 2)) // 2;

        Tri_down = 0;

        Tri_down = ((N - 2 * K + 1) *(N - 2 * K + 2)) // 2;

        return Tri_up + Tri_down;

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, k, expected):
    try:
        if validate_solution(no_of_triangle(
            n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



