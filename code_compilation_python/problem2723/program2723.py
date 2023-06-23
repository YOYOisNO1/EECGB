def program2723():
    F=input()
    M=input()
    S=input()
    
    if(F== "rock" and M == "rock" and S =="rock"):
    	print("?")
    else if(F== "rock" and M == "rock" and S =="paper"):
    	print("S")
    else if(F== "rock" and M == "rock" and S =="scissors"):
    	print("?")
    else if(F== "rock" and M == "paper" and S =="rock"):
    	print("M")
    else if(F== "rock" and M == "paper" and S =="scissors"):
    	print("?")
    else if(F== "rock" and M == "paper" and S =="paper"):
    	print("?")
    else if(F== "rock" and M == "scissors" and S =="rock"):
    	print("?")
    else if(F== "rock" and M == "scissors" and S =="paper"):
    	print("?")
    else if(F== "rock" and M == "scissors" and S =="scissors"):
    	print("F")
    else if(F== "paper" and M == "rock" and S =="rock"):
    	print("F")
    else if(F== "paper" and M == "rock" and S =="paper"):
    	print("?")
    else if(F== "paper" and M == "rock" and S =="scissors"):
    	print("?")
    else if(F== "paper" and M == "paper" and S =="rock"):
    	print("?")
    else if(F== "paper" and M == "paper" and S =="scissors"):
    	print("S")
    else if(F== "paper" and M == "paper" and S =="paper"):
    	print("?")
    else if(F== "paper" and M == "scissors" and S =="rock"):
    	print("?")
    else if(F== "paper" and M == "scissors" and S =="paper"):
    	print("M")
    else if(F== "paper" and M == "scissors" and S =="scissors"):
    	print("?")
    else if(F== "scissors" and M == "rock" and S =="rock"):
    	print("?")
    else if(F== "scissors" and M == "rock" and S =="paper"):
    	print("?")
    else if(F== "scissors" and M == "rock" and S =="scissors"):
    	print("M")
    else if(F== "scissors" and M == "paper" and S =="rock"):
    	print("?")
    else if(F== "scissors" and M == "paper" and S =="scissors"):
    	print("?")
    else if(F== "scissors" and M == "paper" and S =="paper"):
    	print("F")
    else if(F== "scissors" and M == "scissors" and S =="rock"):
    	print("S")
    else if(F== "scissors" and M == "scissors" and S =="paper"):
    	print("?")
    else if(F== "scissors" and M == "scissors" and S =="scissors"):
    	print("?")
    else