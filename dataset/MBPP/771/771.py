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
# Write a function to check if the given expression is balanced or not.
#
# SOLUTION CODE
# ============================================
from collections import deque

def check_expression(exp):

    if len(exp) & 1:

        return False

    stack = deque()

    for ch in exp:

        if ch == '(' or ch == '{' or ch == '[':

            stack.append(ch)

        if ch == ')' or ch == '}' or ch == ']':

            if not stack:

                return False

            top = stack.pop()

            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):

                return False

    return not stack

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(exp, expected):
    try:
        if validate_solution(check_expression(
            exp),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



