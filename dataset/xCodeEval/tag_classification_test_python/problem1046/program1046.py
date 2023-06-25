def cal(n, alice, bob):
        min_alice, max_alice = 0, 0
        
        temp_bob = 0
        for i in range(3):
            alice_i = (i+1)%3
            win = min(bob[i], alice[alice_i])
            draw = min(alice[i], bob[i]-win)
            temp_bob += (win+draw)
    
        for i in range(3):
            bob_i = (i+1)%3
            max_alice += min(alice[i], bob[bob_i])
            
        min_alice = n-temp_bob
        print(min_alice, max_alice)
        
    
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    
    
    cal(n, alice, bob)