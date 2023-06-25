    cal1 = [31,28,31, 30,31,30, 31,31,30, 31,30,31]
    cal2 = [31,29,31, 30,31,30, 31,31,30, 31,30,31]
    cal = cal1*3 + cal2 + cal1*3
    
def main():
        s = input()
        s = input()
        s = [int(x) for x in s.split(' ')]
        for i in range(len(cal)):
            if cal[i] == s[0]:
                if cal[i:i+len(s)] == s:
                    print('Yes')
                    return
        print('No')
    
    if __name__ == '__main__':
        main()