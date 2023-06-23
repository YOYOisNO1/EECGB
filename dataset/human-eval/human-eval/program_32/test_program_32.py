import sys
sys.path.append('../')
from program_32 import poly
from program_32 import find_zero
def test_1():
    assert math.fabs(poly(coeffs, solution)) < 1e-4