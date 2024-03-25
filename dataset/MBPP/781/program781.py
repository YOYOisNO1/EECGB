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
# Write a python function to check whether the count of divisors is even or odd.
#
# SOLUTION CODE
# ============================================
import math 

def count_divisors(n) : 

    count = 0

    for i in range(1, (int)(math.sqrt(n)) + 2) : 

        if (n % i == 0) : 

            if( n // i == i) : 

                count = count + 1

            else : 

                count = count + 2

    if (count % 2 == 0) : 

        return ("Even") 

    else : 

        return ("Odd") 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(count_divisors(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



