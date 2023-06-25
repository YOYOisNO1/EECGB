def program250():
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Mon Nov 26 20:24:39 2018
    
    @author: alexis
    """
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = input()
    count = 0
    for i in word:
        if i in alphabet:
            count += 1
            
    if count > len(word)/2:
        #print('high')
        print(word.lower())
    elif count < len(word)/2:
        #print('low')
        print(word.upper())
    else:
        #print('equal')
        print(word.lower())