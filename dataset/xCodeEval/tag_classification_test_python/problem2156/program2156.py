def program2156():
    a=int(input())
    if any(a%i==0 for i in [4,7,47,74,447,477,474,774,747,744,444,777,44,77]):
        print('YES')
    else:
        str1=str(a)
        list1=list(str1)
        set2=set(list1)
        if set2=={'7','4'}:
            print('YES')
        else:
            print('NO')
            
        
            