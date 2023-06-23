    Skip to content
    Features
    Business
    Explore
    Marketplace
    Pricing
    This repository
    Search
    Sign in or Sign up
    1 3 1 shahed-shd/Online-Judge-Solutions
     Code  Issues 0  Pull requests 0  Projects 0  Insights
    Online-Judge-Solutions/Codeforces/515C - Drazil and Factorial.py
    a01faf7  on Mar 7, 2017
    @shahed-shd shahed-shd Codeforces 515C - Drazil and Factorial.py
         
    51 lines (40 sloc)  1.08 KB
    # ==================================================
    # Problem   :   515C - Drazil and Factorial
    # Run time  :   0.061 sec.
    # Language  :   Python 3
    # ==================================================
    
    
def main():
        from sys import stdin, stdout
    
        # stdin = open("in.txt", "r")
    
        num = stdin.read().split()[1]
    
        ans = []
    
        for d in num:
            if d == '2':
                ans.append('2')
            elif d == '3':
                ans.append('3')
            elif d == '4':
                ans.append('3')
                ans.append('2')
                ans.append('2')
            elif d == '5':
                ans.append('5')
            elif d == '6':
                ans.append('5')
                ans.append('3')
            elif d == '7':
                ans.append('7')
            elif d == '8':
                ans.append('7')
                ans.append('2')
                ans.append('2')
                ans.append('2')
            elif d == '9':
                ans.append('7')
                ans.append('3')
                ans.append('3')
                ans.append('2')
    
        ans.sort(reverse=True)
    
        stdout.write(''.join(ans))
    
    
    if __name__ == '__main__':
        main()
    © 2018 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help
    Contact GitHub
    API
    Training
    Shop
    Blog
    About
    Press h to open a hovercard with more details.