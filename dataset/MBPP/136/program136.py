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
# Write a function to calculate electricity bill.
#
# SOLUTION CODE
# ============================================
def cal_electbill(units):

 if(units < 50):

    amount = units * 2.60

    surcharge = 25

 elif(units <= 100):

    amount = 130 + ((units - 50) * 3.25)

    surcharge = 35

 elif(units <= 200):

    amount = 130 + 162.50 + ((units - 100) * 5.26)

    surcharge = 45

 else:

    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)

    surcharge = 75

 total = amount + surcharge

 return total

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(units, expected):
    try:
        if validate_solution(cal_electbill(
            units),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



