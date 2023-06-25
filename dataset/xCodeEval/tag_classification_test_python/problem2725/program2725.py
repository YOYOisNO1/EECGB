def program2725():
    pt=input()#present time
    sp=input()#sleeping time
    
    pth=int(pt[0:2])
    ptm=int(pt[3:5])
    
    sph=int(sp[0:2])
    spm=int(sp[3:5])
    
    if spm<=ptm:
        pstm=(ptm-spm)
        if pstm<0:
            pstm=pstm+60
        if sph<=pth:
            psth=(pth-sph)
            if psth<0:
                psth=24+psth
        elif sph>pth:
            psth=(24-(sph-pth))
            if psth<0:
                psth=24+psth
    else:
        pstm=(60-(spm-ptm))
        if pstm<0:
            pstm=pstm+60
        if sph<=pth:
            psth=(pth-sph-1)
            if psth<0:
                psth=24+psth
        elif sph>pth:
            psth=(24-(sph-pth)-1)
            if psth<0:
                psth=24+psth
    if pstm<10:
        pstm="0"+str(pstm)
    elif pstm>=10:
        pstm=str(pstm)
    
    if psth<10:
        psth="0"+str(psth)
    elif psth>=10:
        psth=str(psth)
    
    s=psth+":"+pstm
    print(s)
        