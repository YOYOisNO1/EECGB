def program2154():
    s=input()
    if '4' in list(str(s)) and '7' in list(str(s)) and len(set(str(s)))==2:
        print('YES')
        exit()
    elif (s/4>0 and s%4==0) or (s/7>0 and s%7==0)or (s/44>0 and s%44==0)or (s/47>0 and s%47==0)or (s/74>0 and s%74==0)or (s/77>0 and s%77==0)or (s/444>0 and s%444==0)or (s/447>0 and s%447==0)or (s/477>0 and s%477==0)or (s/744>0 and s%744==0)or (s/774>0 and s%774==0)or (s/777>0 and s%777==0):
        print('YES')
    else:
        print('NO')