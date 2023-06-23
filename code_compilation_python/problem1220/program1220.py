def main():
        from sys import stdin, stdout
        dayNum={"saturday" : 0, "sunday" : 1, "monday" : 2, "tuesday" : 3, "wednesday" : 4, "thursday" : 5, "friday" : 6}
        day1, day2=tuple(stdin.read().split())
        day1=dayNum[day1]
        day2=dayNum[day2]
        stdout.write("YES\n" if (day1+28)%7==day2 or or (day1+30)%7 == day2 or (day1+31)%7 == day2 else "NO\n")
        
    if __name__=='__main__':
        main()