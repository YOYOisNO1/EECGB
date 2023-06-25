def main():
        s = input()
        first_one = s.find('1')
        if first_one == -1:
            print('no')
            return
        s = s[first_one:]
        numzeros = len([el for el in s if el == '0'])
        if numzeros >= 6:
            print('yes')
            return
        else:
            print('no')
            return
    main()