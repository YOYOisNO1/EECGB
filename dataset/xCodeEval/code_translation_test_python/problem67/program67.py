def main():
        inpstr = input()
        ans = 0
        tmpans = 1
        vowels = [ 'A', 'E', 'I', 'O', 'U', 'Y' ]
        for ch in inpstr:
            if ch in vowels:
                ans = max( ans, tmpans )
                tmpans = 1
            else:
                tmpans = tmpans + 1
        ans = max( ans, tmpans )
        print(ans) 
    
    if __name__ == "__main__":
        main()