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
# Write a function to check whether the given ip address is valid or not using regex.
#
# SOLUTION CODE
# ============================================
import re 

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

def check_ip(Ip): 

	if(re.search(regex, Ip)): 

		return ("Valid IP address") 

	else: 

		return ("Invalid IP address") 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(ip, expected):
    try:
        if validate_solution(check_ip(
            ip),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



