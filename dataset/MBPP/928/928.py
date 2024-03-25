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
# Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
#
# SOLUTION CODE
# ============================================
import re

def change_date_format(dt):

        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

        return change_date_format(dt)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(dt, expected):
    try:
        if validate_solution(change_date_format(
            dt),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



