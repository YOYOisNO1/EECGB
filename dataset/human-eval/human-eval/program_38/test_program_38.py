import sys
sys.path.append('../')
from program_38 import encode_cyclic
from program_38 import decode_cyclic
def test_1():
    assert decode_cyclic(encoded_str) == str