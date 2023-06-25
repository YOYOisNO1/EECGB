def program2849():
    
    if __name__ == "__main__":
        x = input()
        y = input()
        z = ""
        for i in range(x.__len__()):
            if(y[i] > x[i]):
                z = "-1"
                break
            z = z + y[i]
        
        print(z)