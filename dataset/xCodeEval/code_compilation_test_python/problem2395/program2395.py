def program2395():
    hour,minue = map(int,input().split(':'))
    n = input()
    minue += n%60
    hour += n/60
    if minue >= 60:
        minue -= 60
        hour += 1
    if hour >= 24:
        hour %= 24
    print  str(hour).zfill(2)+':'+str(min