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
# Write a function to find three closest elements from three sorted arrays.
#
# SOLUTION CODE
# ============================================
import sys 



def find_closet(A, B, C, p, q, r): 

	diff = sys.maxsize 

	res_i = 0

	res_j = 0

	res_k = 0

	i = 0

	j = 0

	k = 0

	while(i < p and j < q and k < r): 

		minimum = min(A[i], min(B[j], C[k])) 

		maximum = max(A[i], max(B[j], C[k])); 

		if maximum-minimum < diff: 

			res_i = i 

			res_j = j 

			res_k = k 

			diff = maximum - minimum; 

		if diff == 0: 

			break

		if A[i] == minimum: 

			i = i+1

		elif B[j] == minimum: 

			j = j+1

		else: 

			k = k+1

	return A[res_i],B[res_j],C[res_k]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, c, p, q, r, expected):
    try:
        if validate_solution(find_closet(
            a, b, c, p, q, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



