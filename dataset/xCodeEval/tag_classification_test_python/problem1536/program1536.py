def program1536():
    from itertools import cycle
    s=input()
    t=input()
    track=cycle(list(s))
    position=track.next()
    counter=1
    for i in t:
        if i==position:
            position=track.next()
            counter+=1
    print(counter)
            