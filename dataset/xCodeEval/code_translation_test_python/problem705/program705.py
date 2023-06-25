    class A:
    
    def rotate_keypad(self, keypad):
            reversed_rows = list(reversed(keypad))
            return ["".join(list(reversed(x))) for x in reversed_rows]
    
    def solve(self):
            keypad = [input(), input(), input()]
            if keypad == self.rotate_keypad(keypad):
                print("YES")
            else:
                print("NO")
    
    A().solve()