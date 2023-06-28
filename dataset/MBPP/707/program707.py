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
# Write a python function to count the total set bits from 1 to n.
#
# SOLUTION CODE
# ============================================
def count_set_bits(n) :  

    n += 1; 

    powerOf2 = 2;   

    cnt = n // 2;  

    while (powerOf2 <= n) : 

        totalPairs = n // powerOf2;  

        cnt += (totalPairs // 2) * powerOf2;  

        if (totalPairs & 1) : 

            cnt += (n % powerOf2) 

        else : 

            cnt += 0

        powerOf2 <<= 1;    

    return cnt;  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(count_set_bits(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



