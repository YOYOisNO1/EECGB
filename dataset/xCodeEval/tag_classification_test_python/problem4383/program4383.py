def program4383():
    if __name__ == "__main__":
        s = input()
        s = s.replace('dot', '.')
        ss = s[1:-1]
        ss = ss.replace('at', '@', 1)
        s = s[0] + ss + s[-1]
        if s[0] == '.':
            s = 'dot' + s[1:]
        if s[-1] == '.':
            s = s[:-1] + 'dot'
        print(s)