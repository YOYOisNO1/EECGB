    a=list(map(int,input().split()))
def magic(b):
        for i in range(4):
            if not b[i*4]==b[i*4+2]==b[(i*4+5)%16]==b[(i*4+7)%16] :
                break
        else: print('YES');return
        for i in range(4):
            if not b[4*i+1]==b[4*i+3]==b[(4*i+4)%16]==b[(4*i+6)%16]:
                break
        else: print('YES');return
        print('NO');return
    if a[0]==a[2]==a[3]==a[1] and a[8]==a[10]==a[11]==a[9]:
        magic(a[14]+a[12]+a[15]+a[13]+a[6]+a[4]+a[7]+a[5]+a[18]+a[16]+a[19]+a[17]+a[22]+a[20]+a[23]+a[21])
    elif a[12]==a[14]==a[15]==a[13] and a[16]==a[18]==a[17]==a[19]:
        magic(a[:12]+a[23:19:-1])
    elif a[4]==a[6]==a[7]==a[5] and a[20]==a[22]==a[23]==a[23]:
        magic(a[2]+a[0]+a[3]+a[1]+a[16]+a[17]+a[18]+a[19]+a[9]+a[11]+a[8]+a[10]+a[15]+a[14]+a[13]+a[12])
    else:
        print('NO')