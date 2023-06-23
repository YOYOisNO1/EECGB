def main():
        b = int(input())
        g = int(input())
    
        accepted = int(input())
    
        if b + g == accepted:
            print(1)
            return None
    
        if accepted > b and accepted > g:
            print(min(b, y) - 2)
            return
        
        else:
            print(min(b, g, accepted) + 1)
        
    
    
    if __name__ == "__main__":
        main()