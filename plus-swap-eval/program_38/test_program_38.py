import sys
sys.path.append('../')
from program_38 import encode_cyclic
from program_38 import decode_cyclic
def test_1():
    from random import randint, choice
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_cyclic(str)
        assert decode_cyclic(encoded_str) == str