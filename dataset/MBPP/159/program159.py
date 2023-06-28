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
# Write a function to print the season for the given month and day.
#
# SOLUTION CODE
# ============================================
def month_season(month,days):

 if month in ('January', 'February', 'March'):

	 season = 'winter'

 elif month in ('April', 'May', 'June'):

	 season = 'spring'

 elif month in ('July', 'August', 'September'):

	 season = 'summer'

 else:

	 season = 'autumn'

 if (month == 'March') and (days > 19):

	 season = 'spring'

 elif (month == 'June') and (days > 20):

	 season = 'summer'

 elif (month == 'September') and (days > 21):

	 season = 'autumn'

 elif (month == 'October') and (days > 21):

	 season = 'autumn'

 elif (month == 'November') and (days > 21):

	 season = 'autumn'

 elif (month == 'December') and (days > 20):

	 season = 'winter'

 return season

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(month, days, expected):
    try:
        if validate_solution(month_season(
            month, days),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



