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
# Write a function to find minimum number of coins that make a given value.
#
# SOLUTION CODE
# ============================================
import sys 

def min_coins(coins, m, V): 

    if (V == 0): 

        return 0

    res = sys.maxsize 

    for i in range(0, m): 

        if (coins[i] <= V): 

            sub_res = min_coins(coins, m, V-coins[i]) 

            if (sub_res != sys.maxsize and sub_res + 1 < res): 

                res = sub_res + 1  

    return res 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(coins, m, v, expected):
    try:
        if validate_solution(min_coins(
            coins, m, v),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



