def program2722():
    F=str(input())
    M=str(input())
    W=str(input())
    if F=="rock" and M=="scissors" and W=="scissors":
        print("F")
    elif F=="rock" and M=="paper" and W=="rock":
        print("M")
    elif F=="rock" and M=="rock" and W=="paper":
        print("S")
    elif F=="paper" and M=="rock" and W=="rock":
        print("F")
    elif F=="scissors" and M=="paper" and W=="paper":
        print("F")
    elif F="scissors" and M="scissors" and W="rock":
        print("S")
    else:
        print("?")