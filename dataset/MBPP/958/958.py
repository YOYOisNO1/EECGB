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
# Write a function to convert an integer into a roman numeral.
#
# SOLUTION CODE
# ============================================
def int_to_roman( num):

        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]

        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]

        roman_num = ''

        i = 0

        while  num > 0:

            for _ in range(num // val[i]):

                roman_num += syb[i]

                num -= val[i]

            i += 1

        return roman_num

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num, expected):
    try:
        if validate_solution(int_to_roman(
            num),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



