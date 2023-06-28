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
# Write a function to check whether it follows the sequence given in the patterns array.
#
# SOLUTION CODE
# ============================================
def is_samepatterns(colors, patterns):    

    if len(colors) != len(patterns):

        return False    

    sdict = {}

    pset = set()

    sset = set()    

    for i in range(len(patterns)):

        pset.add(patterns[i])

        sset.add(colors[i])

        if patterns[i] not in sdict.keys():

            sdict[patterns[i]] = []



        keys = sdict[patterns[i]]

        keys.append(colors[i])

        sdict[patterns[i]] = keys



    if len(pset) != len(sset):

        return False   



    for values in sdict.values():



        for i in range(len(values) - 1):

            if values[i] != values[i+1]:

                return False



    return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(colors, patterns, expected):
    try:
        if validate_solution(is_samepatterns(
            colors, patterns),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



