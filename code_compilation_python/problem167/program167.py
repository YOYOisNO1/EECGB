def program167():
    boys=int(input())
    girls=int(input())
    n=int(input())
    decks=n+1
    deck=[]
    for i in range(0,n+1):
        blue=i
        red=n-i
        if(blue>boys or red>girls):
            continue
        deck.append(1)
    print(count(deck))