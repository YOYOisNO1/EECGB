    import fileinput
    
def solve(level):
        level = [l == "*" for l in level]
    def test(start, step):
            count = 0
            for val in level[start::step]:
                if val:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
            return False
        for step in range(1, int((len(level)) / 4 + 1)):
            for start in range(step):
                if test(start, step):
                    return True
        return False
    
    if __name__ == '__main__':
        data = list(iter(fileinput.input()))
        level = data[1]
        if solve(level):
            print("yes")
        else:
            print("no")