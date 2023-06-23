def program281():
    times=input().split(" ")
    scors=input().split(" ")
    place=int(scors[int(times[1])])
    counter=0
    for i in scors:
        while int(i)>=place and place!=0:
            counter=counter+1
    print(counter)