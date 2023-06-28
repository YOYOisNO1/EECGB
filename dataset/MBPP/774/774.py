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
# Write a function to check if the string is a valid email address or not using regex.
#
# SOLUTION CODE
# ============================================
import re 

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check_email(email): 

	if(re.search(regex,email)): 

		return ("Valid Email") 

	else: 

		return ("Invalid Email") 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(email, expected):
    try:
        if validate_solution(check_email(
            email),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



