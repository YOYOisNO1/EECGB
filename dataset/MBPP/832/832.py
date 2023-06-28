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
# Write a function to extract the maximum numeric value from a string by using regex.
#
# SOLUTION CODE
# ============================================
import re 

def extract_max(input): 

	numbers = re.findall('\d+',input) 

	numbers = map(int,numbers) 

	return max(numbers)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(input, expected):
    try:
        if validate_solution(extract_max(
            input),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



