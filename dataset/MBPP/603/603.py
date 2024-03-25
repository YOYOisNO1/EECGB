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
# Write a function to get a lucid number smaller than or equal to n.
#
# SOLUTION CODE
# ============================================
def get_ludic(n):

	ludics = []

	for i in range(1, n + 1):

		ludics.append(i)

	index = 1

	while(index != len(ludics)):

		first_ludic = ludics[index]

		remove_index = index + first_ludic

		while(remove_index < len(ludics)):

			ludics.remove(ludics[remove_index])

			remove_index = remove_index + first_ludic - 1

		index += 1

	return ludics

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(get_ludic(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



