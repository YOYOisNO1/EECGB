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
# Write a python function to count the total unset bits from 1 to n.
#
# SOLUTION CODE
# ============================================
def count_unset_bits(n) :  

    cnt = 0;  

    for i in range(1,n + 1) : 

        temp = i;  

        while (temp) :  

            if (temp % 2 == 0) : 

                cnt += 1;  

            temp = temp // 2;  

    return cnt;  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(count_unset_bits(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



