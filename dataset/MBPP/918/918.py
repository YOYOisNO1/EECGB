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
# Write a function to count coin change.
#
# SOLUTION CODE
# ============================================
def coin_change(S, m, n): 

    table = [[0 for x in range(m)] for x in range(n+1)] 

    for i in range(m): 

        table[0][i] = 1

    for i in range(1, n+1): 

        for j in range(m): 

            x = table[i - S[j]][j] if i-S[j] >= 0 else 0

            y = table[i][j-1] if j >= 1 else 0 

            table[i][j] = x + y   

    return table[n][m-1] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, m, n, expected):
    try:
        if validate_solution(coin_change(
            s, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



