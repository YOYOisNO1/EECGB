def program3149():
    #!/usr/bin/python
    
    n,k = map(int, input().split())
    answer=1
    
    if k>1:
        answer += n*(n-1)/2
    if k>2:
        answer += n*(n-1)*(n-2)/3
    if k>3:
        answer += n*(n-1)*(n-2)*(n-3)/24*9
    
    print(int(answer))