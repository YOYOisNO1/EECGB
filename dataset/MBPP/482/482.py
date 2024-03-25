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
# Write a function to find sequences of one upper case letter followed by lower case letters in the given string by using regex.
#
# SOLUTION CODE
# ============================================
import re 

def match(text): 

		pattern = '[A-Z]+[a-z]+$'

		if re.search(pattern, text): 

				return('Yes') 

		else: 

				return('No') 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, expected):
    try:
        if validate_solution(match(
            text),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



