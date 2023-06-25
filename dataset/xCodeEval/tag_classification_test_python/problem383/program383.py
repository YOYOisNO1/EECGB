def program383():
    #n = map(int,input().split())
    #list_n = list(map(str,input().split()))
    #list_m = list(map(str,input().split()))
    queries = input()
    if(queries.count('a')> len(queries)/2):
        print(len(queries))
    else:
        print(2*queries.count('a')-1)
        
    #for query in range(queries):