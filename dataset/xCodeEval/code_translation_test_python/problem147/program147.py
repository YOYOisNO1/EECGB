def f():v=input();return 60*int(v[:2])+int(v[-2:])
    x=f()-f()
    print"%02d:%02d"%(x/60%24,x%60)