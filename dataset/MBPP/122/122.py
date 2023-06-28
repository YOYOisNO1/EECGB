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
# Write a function to find nth smart number.
#
# SOLUTION CODE
# ============================================
MAX = 3000 

def smart_number(n): 

	primes = [0] * MAX 

	result = [] 

	for i in range(2, MAX): 

		if (primes[i] == 0): 

			primes[i] = 1 

			j = i * 2 

			while (j < MAX): 

				primes[j] -= 1 

				if ( (primes[j] + 3) == 0): 

					result.append(j) 

				j = j + i 

	result.sort() 

	return result[n - 1] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(smart_number(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



