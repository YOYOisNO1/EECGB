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
# Write a function to check if there is a subset with sum divisible by m.
#
# SOLUTION CODE
# ============================================
def modular_sum(arr, n, m): 

	if (n > m): 

		return True

	DP = [False for i in range(m)] 

	for i in range(n): 

		if (DP[0]): 

			return True

		temp = [False for i in range(m)] 

		for j in range(m): 

			if (DP[j] == True): 

				if (DP[(j + arr[i]) % m] == False): 

					temp[(j + arr[i]) % m] = True

		for j in range(m): 

			if (temp[j]): 

				DP[j] = True

		DP[arr[i] % m] = True

	return DP[0]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, m, expected):
    try:
        if validate_solution(modular_sum(
            arr, n, m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



