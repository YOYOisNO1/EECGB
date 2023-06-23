def program158():
    word = input()
    counter = 1
    for i in range(len(word)-1):
        while word[i]==word[i+1]:
            counter +=1
        else:
            counter=1
        if counter == 7:
            print("YES")
    print("NO")