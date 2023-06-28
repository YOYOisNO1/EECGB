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
# Write a function to find perfect squares between two given numbers.
#
# SOLUTION CODE
# ============================================
def perfect_squares(a, b):

    lists=[]

    for i in range (a,b+1):

        j = 1;

        while j*j <= i:

            if j*j == i:

                 lists.append(i)  

            j = j+1

        i = i+1

    return lists

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, expected):
    try:
        if validate_solution(perfect_squares(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



