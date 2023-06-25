def solve():
        tokens = input().split(" ")
        a = int(tokens[0])
        b = int(tokens[1])
        m = int(tokens[2])
        r = int(tokens[3])
        lastVisit = []
        for i in range(0, m):
            lastVisit.append(-1)
        lastVisit[r] = 0
        index = 1
        while True:
            r = (r*a+b)%m
            if not lastVisit[r] == -1:
                print(index - lastVisit[r])
                return
            lastVisit[r] = index
            index += 1
    
    if __name__ == "__main__":
        solve()