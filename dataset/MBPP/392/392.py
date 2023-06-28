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
# Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
#
# SOLUTION CODE
# ============================================
def get_max_sum (n):

	res = list()

	res.append(0)

	res.append(1)

	i = 2

	while i<n + 1:

		res.append(max(i, (res[int(i / 2)] 

						+ res[int(i / 3)] +

							res[int(i / 4)]

						+ res[int(i / 5)])))

		i = i + 1

	return res[n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution((
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



