    #!/usr/bin/env python
    
    
def main():
        moves = input()
    
        visited = set()
        x = y = 0
        last = x, y
        for m in moves:
            if m == "L":
                x -= 1
            elif m == "R":
                x += 1
            elif m == "U":
                y += 1
            else:
                y -= 1
            curr = x, y
            for pos in curr, (x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1):
                if pos in visited:
                    print("BUG")
                    return
            visited.add(last)
            last = curr
        print("OK")
    
    
    if __name__ == '__main__':
        main()