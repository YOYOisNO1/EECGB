def program6095():
    #!/usr/bin/env	python
    #-*-coding:utf-8 -*-
    z=input()
    M='fedabc'
    n=int(z.rstrip(M))-1
    print(1+M.find(z[-1])+7*(1&n)|n>>2<<4)