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
# Write a python function to convert decimal number to octal number.
#
# SOLUTION CODE
# ============================================
def decimal_to_octal(deciNum):

    octalNum = 0

    countval = 1;

    dNo = deciNum;

    while (deciNum!= 0):

        remainder= deciNum % 8;

        octalNum+= remainder*countval;

        countval= countval*10;

        deciNum //= 8; 

    return (octalNum)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(decinum, expected):
    try:
        if validate_solution(decimal_to_octal(
            decinum),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



