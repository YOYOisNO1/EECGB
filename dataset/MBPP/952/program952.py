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
# Write a function to compute the value of ncr mod p.
#
# SOLUTION CODE
# ============================================
def n_cr_mod_p(n, r, p): 

	if (r > n- r): 

		r = n - r 

	C = [0 for i in range(r + 1)] 

	C[0] = 1 

	for i in range(1, n + 1): 

		for j in range(min(i, r), 0, -1): 

			C[j] = (C[j] + C[j-1]) % p 

	return C[r] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, r, p, expected):
    try:
        if validate_solution(n_cr_mod_p(
            n, r, p),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



