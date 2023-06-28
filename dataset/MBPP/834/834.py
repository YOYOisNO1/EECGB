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
# Write a function to generate a square matrix filled with elements from 1 to n raised to the power of 2 in spiral order.
#
# SOLUTION CODE
# ============================================
def generate_matrix(n):

        if n<=0:

            return [] 

        matrix=[row[:] for row in [[0]*n]*n]        

        row_st=0

        row_ed=n-1        

        col_st=0

        col_ed=n-1

        current=1        

        while (True):

            if current>n*n:

                break

            for c in range (col_st, col_ed+1):

                matrix[row_st][c]=current

                current+=1

            row_st+=1

            for r in range (row_st, row_ed+1):

                matrix[r][col_ed]=current

                current+=1

            col_ed-=1

            for c in range (col_ed, col_st-1, -1):

                matrix[row_ed][c]=current

                current+=1

            row_ed-=1

            for r in range (row_ed, row_st-1, -1):

                matrix[r][col_st]=current

                current+=1

            col_st+=1

        return matrix

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(generate_matrix(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



