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
# Write a function to get the word with most number of occurrences in the given strings list.
#
# SOLUTION CODE
# ============================================
from collections import defaultdict 



def most_occurrences(test_list):

  temp = defaultdict(int)

  for sub in test_list:

    for wrd in sub.split():

      temp[wrd] += 1

  res = max(temp, key=temp.get)

  return (str(res)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(most_occurrences(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



