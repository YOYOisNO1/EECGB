import sys
sys.path.append('../')
from program_50 import encode_shift
from program_50 import decode_shift
def test_1():
    assert decode_shift(copy.deepcopy(encoded_str)) == str