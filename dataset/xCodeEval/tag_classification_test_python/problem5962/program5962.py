def program5962():
    c,H,h,W,w=map(int,input().split())
    if W*W>=c or w*w>=c:
      if w>W:H,h,W,w=h,H,w,W
      I=c/W+1
    else:
      if H*w>h*W:H,h,W,w=h,H,w,W
      I=w
    print(max(i*H+(c-i*W)/w*h) for i in range(I))
    