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
# Write a function to calculate magic square.
#
# SOLUTION CODE
# ============================================
def magic_square_test(my_matrix):

    iSize = len(my_matrix[0])

    sum_list = []

    sum_list.extend([sum (lines) for lines in my_matrix])   

    for col in range(iSize):

        sum_list.append(sum(row[col] for row in my_matrix))

    result1 = 0

    for i in range(0,iSize):

        result1 +=my_matrix[i][i]

    sum_list.append(result1)      

    result2 = 0

    for i in range(iSize-1,-1,-1):

        result2 +=my_matrix[i][i]

    sum_list.append(result2)

    if len(set(sum_list))>1:

        return False

    return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(my_matrix, expected):
    try:
        if validate_solution(magic_square_test(
            my_matrix),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



