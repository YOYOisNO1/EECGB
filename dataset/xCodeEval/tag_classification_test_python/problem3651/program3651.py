def program3651():
    n, t = input().split(" ")
    
    string = input()
    
    for i in range(int(t)):
        string = string.replace("BG", "GB")
    
    print(string)