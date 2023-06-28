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
# Write a python function to count the pairs with xor as an odd number.
#
# SOLUTION CODE
# ============================================
def find_odd_pair(A,N) : 

    oddPair = 0

    for i in range(0,N) :  

        for j in range(i+1,N) :  

            if ((A[i] ^ A[j]) % 2 != 0):  

                oddPair+=1  

    return oddPair  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, expected):
    try:
        if validate_solution(find_odd_pair(
            a, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



