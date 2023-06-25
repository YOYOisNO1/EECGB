    import sys
    from collections import defaultdict
    mod = 1000000007
def get_array(): return list(map(int, sys.stdin.readline().split()))
def get_ints(): return map(int, sys.stdin.readline().split())
def input(): return sys.stdin.readline()
def print_array(a): print(" ".join(map(str, a)))
def main():
        a, b, x, y = get_ints()
        m = []
        if a == x or b == y: m.append(1)
        else: m.append(2)
        if (a + b) % 2 != (x + y) % 2: m.append(0)
        else:
            if (a + b) == (x + y) or a - b == x - y: m.append(1)
            else: m.append(2)
        m.append(abs(a - x) if abs(a - x) > abs(b - y) else abs(b - y))
        print_array(m)
    if __name__ == "__main__":
        main()