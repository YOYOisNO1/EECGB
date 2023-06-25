def program1043():
    
    no = int(input())
    
    alice_rock, alice_scissors, alice_paper = list(map(int, input().split()))
    bob_rock, bob_scissors, bob_paper = list(map(int, input().split()))
    
    my_max = min(alice_rock, bob_scissors) + min(alice_scissors, bob_paper) + min(alice_paper, bob_rock)
    my_min = min(alice_rock, no - bob_scissors) + min(alice_scissors, no - bob_paper) + min(alice_paper, no - bob_rock)
    
    print(no - my_min, my_max)