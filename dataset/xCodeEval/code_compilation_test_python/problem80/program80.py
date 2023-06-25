def final(string1,string2):
        string1=string1.lower()
        string2=string2.lower()
        for i in range(len(string1)):
            if string1[i]==string2[i]:
                continue
            elif string1[i]<string2[i]:
                return -1
            elif string1[i]>string2[i]:
                return 1
        return 0
    
    string1=input()
    string2=input()
    print(final(string1,string2))