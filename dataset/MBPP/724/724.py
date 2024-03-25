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
# Write a function to calculate the sum of all digits of the base to the specified power.
#
# SOLUTION CODE
# ============================================
def power_base_sum(base, power):

    return sum([int(i) for i in str(pow(base, power))])

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(base_arg0, power, expected):
    try:
        if validate_solution(power_base_sum(
            base_arg0, power),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



