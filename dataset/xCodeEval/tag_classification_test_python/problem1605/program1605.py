def program1605():
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Fri Jun 23 16:12:17 2017
    
    @author: umang
    """
    
    x1, y1, x2, y2 = map(int, input().split())
    a, b = map(int, input().split())
    if((((y2-y1)/b)%2==((x2-x1)/a)%2) and ((y2-y1)%b == (x2-x1)%a == 0)):
        print("YES")
    else:
        print("NO")