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
# Write a function to calculate distance between two points using latitude and longitude.
#
# SOLUTION CODE
# ============================================
from math import radians, sin, cos, acos

def distance_lat_long(slat,slon,elat,elon):

 dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))

 return dist

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-09

def driver(slat, slon, elat, elon, expected):
    try:
        if validate_solution(distance_lat_long(
            slat, slon, elat, elon),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



