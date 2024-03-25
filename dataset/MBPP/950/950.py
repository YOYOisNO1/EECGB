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
# Write a function to display sign of the chinese zodiac for given year.
#
# SOLUTION CODE
# ============================================
def chinese_zodiac(year):

 if (year - 2000) % 12 == 0:

     sign = 'Dragon'

 elif (year - 2000) % 12 == 1:

     sign = 'Snake'

 elif (year - 2000) % 12 == 2:

     sign = 'Horse'

 elif (year - 2000) % 12 == 3:

     sign = 'sheep'

 elif (year - 2000) % 12 == 4:

     sign = 'Monkey'

 elif (year - 2000) % 12 == 5:

     sign = 'Rooster'

 elif (year - 2000) % 12 == 6:

     sign = 'Dog'

 elif (year - 2000) % 12 == 7:

     sign = 'Pig'

 elif (year - 2000) % 12 == 8:

     sign = 'Rat'

 elif (year - 2000) % 12 == 9:

     sign = 'Ox'

 elif (year - 2000) % 12 == 10:

     sign = 'Tiger'

 else:

     sign = 'Hare'

 return sign

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(year, expected):
    try:
        if validate_solution(chinese_zodiac(
            year),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



