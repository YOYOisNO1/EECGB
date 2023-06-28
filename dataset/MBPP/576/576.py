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
# Write a python function to check whether an array is subarray of another or not.
#
# SOLUTION CODE
# ============================================
def is_sub_array(A,B,n,m): 

    i = 0; j = 0; 

    while (i < n and j < m):  

        if (A[i] == B[j]): 

            i += 1; 

            j += 1; 

            if (j == m): 

                return True;  

        else: 

            i = i - j + 1; 

            j = 0;       

    return False; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, n, m, expected):
    try:
        if validate_solution(is_sub_array(
            a, b, n, m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



