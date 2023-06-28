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
# Write a function to find the demlo number for the given number.
#
# SOLUTION CODE
# ============================================
def find_demlo(s): 

	l = len(s) 

	res = "" 

	for i in range(1,l+1): 

		res = res + str(i) 

	for i in range(l-1,0,-1): 

		res = res + str(i) 

	return res 	

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(find_demlo(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



