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
# Write a function to find out the second most repeated (or frequent) string in the given sequence.
#
# SOLUTION CODE
# ============================================
from collections import Counter 

	

def second_frequent(input): 

	dict = Counter(input) 

	value = sorted(dict.values(), reverse=True)  

	second_large = value[1] 

	for (key, val) in dict.items(): 

		if val == second_large: 

			return (key) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(input, expected):
    try:
        if validate_solution(second_frequent(
            input),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



