def program2434():
    rubik= list(map(int,input().split()))
    a=[0]
    for i in rubik:
        a.append(i)
    if a[1]==a[3]==a[6]==a[8] and a[2]==a[4]==a[22]==a[24] and a[5]==a[7]==a[10]==a[12]  and a[13]==a[14]==a[15]==a[16] and a[9]==a[11]==a[21]==a[23]:
        print('YES')
        exit(0)
        if a[1]==a[12]==a[18]==a[8] and a[5]==a[17]==a[11]==a[16] and a[13]==a[15]==a[6]==a[23]  and a[3]==a[19]==a[22]==a[24] and a[4]==a[7]==a[20]==a[21]:
        print('YES')
        exit(0)
    print("NO")