import sys
sys.path.append('../')
from program_74 import total_match
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert total_match([], []) == []
def test_3():
    assert total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
def test_4():
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
def test_5():
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
def test_6():
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
def test_7():
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
def test_8():
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']
def test_9():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_10():
    assert total_match([], ['this']) == []
def test_11():
    assert total_match(['this'], []) == []