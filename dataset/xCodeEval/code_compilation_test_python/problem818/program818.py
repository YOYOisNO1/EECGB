def program818():
    a=input()
    home=input()
    c=1
    for e in range(a):
        c+=input().endswith(home)
    if !(c % 2):
        print "contest"
    else:
        print "home"