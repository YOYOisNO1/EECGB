

def max_element(l: list):
    

    assert all(type(x) in [int, float] for x in l), "invalid inputs"
    return max(l)

