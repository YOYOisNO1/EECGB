def program6341():
    hpy,atky,defy = input().split(" ")
    hpm,atkm,defm = input().split(" ")
    h,a,d = input().split(" ")
    hpy,atky,defy = int(hpy),int(atky),int(defy)
    hpm,atkm,defm = int(hpm),int(atkm),int(defm)
    h,a,d = int(h),int(a),int(d)
    
    
    cost = 1000000
    for i in range(0,max(0,100-atky+defm)+1):
        for j in range(0,max(0,atkm-defy)+1):
            if i+atky-defm>0:
                turn = hpm/(i+atky-defm)
                if hpm%(i+atky-defm)!=0:
                    turn+=1
                damage = max(0,turn*(atkm-defy-j)+1-hpy)
                cost = min(cost,damage*h+i*a+j*d)
    print(cost)