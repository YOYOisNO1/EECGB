import sys
sys.path.append('../')
from program_149 import sorted_list_sum
def test_1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
def test_2():
    assert sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
def test_3():
    assert sorted_list_sum(["d", "b", "c", "a"]) == []
def test_4():
    assert sorted_list_sum(["d", "dcba", "abcd", "a"]) == ["abcd", "dcba"]
def test_5():
    assert sorted_list_sum(["AI", "ai", "au"]) == ["AI", "ai", "au"]
def test_6():
    assert sorted_list_sum(["a", "b", "b", "c", "c", "a"]) == []
def test_7():
    assert sorted_list_sum(['aaaa', 'bbbb', 'dd', 'cc']) == ["cc", "dd", "aaaa", "bbbb"]