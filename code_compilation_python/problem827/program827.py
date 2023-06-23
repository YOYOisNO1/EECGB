def program827():
    n=input()
    strs=input()
    k='ogo'
    while True:
        while k in strs:
            k+='go'
        k=[:-2]
        strs=strs.replace(k,'***')
        if k=='ogo':
            print(strs)
            break
        else:
            k=='ogo'