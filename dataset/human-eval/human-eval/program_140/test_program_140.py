import sys
sys.path.append('../')
from program_140 import fix_spaces
def test_1():
    assert fix_spaces("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert fix_spaces("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
def test_3():
    assert fix_spaces("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
def test_4():
    assert fix_spaces("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
def test_5():
    assert fix_spaces("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"