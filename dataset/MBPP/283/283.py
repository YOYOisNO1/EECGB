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
# Write a python function to check whether the frequency of each digit is less than or equal to the digit itself.
#
# SOLUTION CODE
# ============================================
def validate(n): 

    for i in range(10): 

        temp = n;  

        count = 0; 

        while (temp): 

            if (temp % 10 == i): 

                count+=1;  

            if (count > i): 

                return False

            temp //= 10; 

    return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(validate(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



