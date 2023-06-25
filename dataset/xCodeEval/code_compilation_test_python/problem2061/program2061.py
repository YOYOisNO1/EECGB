def program2061():
    import sys
    
    if __name__ == "__main__":
        a = sys.stdin.readline.rstrip().split(' ')
        count = int(a[0])
        jump = int(a[1])
        s = sys.stdin.readline.rstrip()
        grasshopper_location = s.find('G')
        target_location = s.find('T')
        r = "YES"
        if abs(grasshopper_location - target_location) % jump != 0:
            print('NO')
        else:
            if grasshopper_location > target_location:
                i = grasshopper_location - jump
                while i > target_location:
                    if s[i] == '#':
                        r = "NO"
                        break
                    i -= jump
            else:
                i = grasshopper_location + jump
                while i < target_location:
                    if s[i] == '#'
                        r = "NO"
                        break
                    i += jump
            print(r)