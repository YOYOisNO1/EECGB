def program3120():
    n= input();
    s=input();
    z=s.split ("0");
    decodednum=0;
    for a in z:
     decodednum*=10;
     decodednum+=len (a);
    print decodednum