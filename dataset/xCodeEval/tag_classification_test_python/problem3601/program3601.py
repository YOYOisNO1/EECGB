def program3601():
    n, t = map(int, input().split())
    entrada = input()
    
    for i in range(t):
    	entrada = entrada.replace("BG","GB")
    
    print(entrada)