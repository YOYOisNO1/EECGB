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
# Write a function to find the nth super ugly number from a given prime list of size k using heap queue algorithm.
#
# SOLUTION CODE
# ============================================
import heapq

def nth_super_ugly_number(n, primes):

    uglies = [1]

    def gen(prime):

        for ugly in uglies:

            yield ugly * prime

    merged = heapq.merge(*map(gen, primes))

    while len(uglies) < n:

        ugly = next(merged)

        if ugly != uglies[-1]:

            uglies.append(ugly)

    return uglies[-1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, primes, expected):
    try:
        if validate_solution(nth_super_ugly_number(
            n, primes),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



