def program1384():
    from collections import Counter
    
    if __name__ == "__main__":
        num = input()
        digitMap = Counter(num)
        c= digitMap['4']+digitMap['7']
        if(c==4 or c==7):
            print("YES")
        else:
            print("NO")