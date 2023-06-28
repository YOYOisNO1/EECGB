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
# Write a function to find if the given number is a keith number or not.
#
# SOLUTION CODE
# ============================================
def is_num_keith(x): 

	terms = [] 

	temp = x 

	n = 0 

	while (temp > 0): 

		terms.append(temp % 10) 

		temp = int(temp / 10) 

		n+=1 

	terms.reverse() 

	next_term = 0 

	i = n 

	while (next_term < x): 

		next_term = 0 

		for j in range(1,n+1): 

			next_term += terms[i - j] 

		terms.append(next_term) 

		i+=1 

	return (next_term == x) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, expected):
    try:
        if validate_solution(is_num_keith(
            x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



