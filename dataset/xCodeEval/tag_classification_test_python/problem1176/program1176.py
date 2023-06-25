def program1176():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Feb 13 22:43:54 2020
    
    @author: jared
    """
    
    column, row = input()
    column_edge, row_edge = column in ['a', 'h'], row in ['1', '8']
    if column_edge and row_edge:
        print(3)
    elif column_edge or row_edge:
        print(5)
    else:
        print(8)