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
# Write a function to check whether the given string is ending with only alphanumeric characters or not using regex.
#
# SOLUTION CODE
# ============================================
import re 

regex = '[a-zA-z0-9]$'

def check_alphanumeric(string): 

	if(re.search(regex, string)): 

		return ("Accept") 

	else: 

		return ("Discard") 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, expected):
    try:
        if validate_solution(check_alphanumeric(
            string_arg0),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



