def program3295():
    dat = input().strip().split(' ')
    dat = [int(x) for x in dat]
    lft = (dat[1]+2+dat[3])
    top = dat[0] + 1
    bot = dat[2] + 1
    rig = dat[1] + dat[3] + abs(dat[0] - dat[2])
    print(lft + top + bot + rig, end='')