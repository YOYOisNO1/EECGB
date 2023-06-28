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
# Write a function to find if there is a triplet in the array whose sum is equal to a given value.
#
# SOLUTION CODE
# ============================================
def find_triplet_array(A, arr_size, sum): 

	for i in range( 0, arr_size-2): 

		for j in range(i + 1, arr_size-1): 

			for k in range(j + 1, arr_size): 

				if A[i] + A[j] + A[k] == sum: 

					return  A[i],A[j],A[k] 

					return True

	return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, arr_size, sum, expected):
    try:
        if validate_solution(find_triplet_array(
            a, arr_size, sum),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



