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
# Write a function that gives profit amount if the given amount has profit else return none.
#
# SOLUTION CODE
# ============================================
def profit_amount(actual_cost,sale_amount): 

 if(actual_cost > sale_amount):

    amount = actual_cost - sale_amount

    return amount

 else:

    return None

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(actual_cost, sale_amount, expected):
    try:
        if validate_solution(profit_amount(
            actual_cost, sale_amount),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



