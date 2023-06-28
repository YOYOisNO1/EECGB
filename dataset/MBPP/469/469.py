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
# Write a function to find the maximum profit earned from a maximum of k stock transactions
#
# SOLUTION CODE
# ============================================
def max_profit(price, k):

    n = len(price)

    final_profit = [[None for x in range(n)] for y in range(k + 1)]

    for i in range(k + 1):

        for j in range(n):

            if i == 0 or j == 0:

                final_profit[i][j] = 0

            else:

                max_so_far = 0

                for x in range(j):

                    curr_price = price[j] - price[x] + final_profit[i-1][x]

                    if max_so_far < curr_price:

                        max_so_far = curr_price

                final_profit[i][j] = max(final_profit[i][j-1], max_so_far)

    return final_profit[k][n-1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(price, k, expected):
    try:
        if validate_solution(max_profit(
            price, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



