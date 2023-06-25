def program3137():
    if __name__ == '__main__':
        n = input()
        if int(n[len(n)-1]) <= 5:
            print(n[:len(n)-1]+'0')
        elif int(n[len(n)-1]) >= 6:
            print(str(int(n)+(10 - int(n[len(n)-1]))))