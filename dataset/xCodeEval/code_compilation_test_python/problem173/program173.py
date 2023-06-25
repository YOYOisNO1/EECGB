    import unittest
    
def solve(a,b):
        if a == b:
            return 1
    
        if b == 1:
            return a
    
        a -= b
        if b > a:
            a,b = b,a
    
        return 1 + solve(a,b)
    
    class Test_solution(unittest.TestCase):
    def test_case(self):
            self.assertEqual(solve(2,2), 1)
            self.assertEqual(solve(2,1), 2)
            self.assertEqual(solve(10,7), 6)
            self.assertEqual(solve(1000000000000, 1), 1000000000000)
    
    
    
    if __name__ == '__main__':
        #unittest.main()
        a, b = map(int, input().split())
        print(solve(a,b))