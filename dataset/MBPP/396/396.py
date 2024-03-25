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
# Write a function to check whether the given string starts and ends with the same character or not using regex.
#
# SOLUTION CODE
# ============================================
import re  

regex = r'^[a-z]$|^([a-z]).*\1$'

def check_char(string): 

	if(re.search(regex, string)): 

		return "Valid" 

	else: 

		return "Invalid" 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, expected):
    try:
        if validate_solution(check_char(
            string_arg0),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



