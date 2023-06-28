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
# Write a python function to count the pairs with xor as an even number.
#
# SOLUTION CODE
# ============================================
def find_even_pair(A,N): 

    evenPair = 0

    for i in range(0,N): 

        for j in range(i+1,N): 

            if ((A[i] ^ A[j]) % 2 == 0): 

                evenPair+=1

    return evenPair; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, expected):
    try:
        if validate_solution(find_even_pair(
            a, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



