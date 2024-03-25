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
# Write a function to check whether the given amount has no profit and no loss
#
# SOLUTION CODE
# ============================================
def noprofit_noloss(actual_cost,sale_amount): 

  if(sale_amount == actual_cost):

    return True

  else:

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(actual_cost, sale_amount, expected):
    try:
        if validate_solution(noprofit_noloss(
            actual_cost, sale_amount),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



