def program1875():
    num_floor=input('')
    num_floor=int(num_floor)
    floor_count=input('')
    floor_count_list=floor_count.split(' ')
    floor_count_list=[int(x) for x in floor_count_list]
    floor=0
    if floor_count_list[0]!=0:
        max_ppl=1
    else:
        max_ppl=floor_count_list.index(max(floor_count_list))+1
    result=0
    electricty_count=0
    for numppl in floor_count_list:
        floor+=1
        if numppl!=0:
            
            floor_drive=abs(floor-max_ppl)
            floor_drive+=abs(max_ppl-1)
            floor_drive=floor_drive*2
            electricty_count+=numppl*(floor_drive+(2*(floor-1)))
    
    
    
    print(electricty_count)