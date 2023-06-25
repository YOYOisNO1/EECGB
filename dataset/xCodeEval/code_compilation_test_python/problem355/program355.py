def program355():
    n = int(input())
    fir = list(map(int, input().split()))
    sec = list(map(int, input().split()))
    fir.pop(0)
    sec.pop(0)
    
    fir_saved = ''.join(fir)
    sec_saved = ''.join(sec)
    
    fight_cnt = 0
    impossible = False
    while(fir and sec):
        fir_card = fir.pop(0)
        sec_card = sec.pop(0)
    
        if(fir_card > sec_card):
            fir.append(sec_card)
            fir.append(fir_card)
        else:
            sec.append(fir_card)
            sec.append(sec_card)
    
        fight_cnt += 1
    
        if fir_saved == ''.join(fir) and sec_saved == ''.join(sec):
            impossible = True
            break
    
    if impossible:
        print(-1)
    else:
        print(fight_cnt, 1 if fir else 2)