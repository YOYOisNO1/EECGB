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
# Write a function to count unique keys for each value present in the tuple.
#
# SOLUTION CODE
# ============================================
from collections import defaultdict 

def get_unique(test_list):

  res = defaultdict(list)

  for sub in test_list:

    res[sub[1]].append(sub[0])

  res = dict(res)

  res_dict = dict()

  for key in res:

    res_dict[key] = len(list(set(res[key])))

  return (str(res_dict)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(get_unique(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



