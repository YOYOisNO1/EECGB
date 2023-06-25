def program2376():
    n=input()
    s='+'+'-'*24+'+'
    print(s)
    x= (n>0) if n<=4 else 1 + (n-2)/3
    print('|')+'O.'*x+'#.'*(11-x)+'|D|)'
    x= (n>1) if n<=4 else 1 + (n-3)/3
    print('|')+'O.'*x+'#.'*(11-x)+'|.|'
    print('|')+('O' if n>2 else '#')+'.'*23+'|'
    x=(n==4)if n<=4 else 1 + (n-4)/3
    print('|')+'O.'*x+'#.'*(11-x)+'|.|)'
    print(s)