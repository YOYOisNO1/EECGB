def program3215():
    a=input()
    b=a[0:1]
    d=a[1:]
    c=ord(b)
    if c>=97 and c<=122 :
        c=c-32
    sum=chr(c)+d
    print(sum)