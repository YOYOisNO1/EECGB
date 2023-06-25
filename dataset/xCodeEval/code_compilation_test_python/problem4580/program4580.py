def program4580():
    user_input=int(input())
    cards=input()
    cards_array=cards.split(' ')
    colours=['R','G','B','Y','W']
    values=['1','2','3','4','5']
    
    card_set=set(cards_array)
    if len(card_set)==1:
        print ("0")
    else:
        colour_array=[]
        value_array=[]
    
        for card in card_set:
            colour_array.extend([card[0]])
            value_array.extend([card[1]])
    
        hint_list=[]
        hints=0
    
        known=0
    
        colour_hint=0
        value_hint=0
    
        for the_colour in colours:
            if colour_array.count(the_colour) == len(card_set):
                for i in range(len(card_set)):
                    colour_array[i]='known'
                hint_list.extend(the_colour)
                colour_hint+=1
    
            elif colour_array.count(the_colour) == 0:
                hint_list.extend(the_colour)
                colour_hint+=1
    
        for the_value in values:
            if value_array.count(the_value) == len(card_set):
                for i in range(len(card_set)):
                    value_array[i] = 'known'
                hint_list.extend(the_value)
                value_hint+=1
    
            elif value_array.count(the_value)==0:
                hint_list.extend(the_value)
                value_hint+=1
    
        while known<(len(card_set)):
            count=0
            for the_value in values:
                if the_value in hint_list:
                    pass
                else:
                    if value_array.count(the_value)>count:
                        index=values.index(the_value)
                        count=value_array.count(the_value)
    
            if count!=0:
                hints+=1
                value_hint+=1
                hint_list.extend(values[index])
                another_count=value_array.count(values[index])
                for i in range(value_array.count(values[index])):
                        an_index=value_array.index(values[index])
                        value_array[an_index]='known'
    
                        if colour_array[index] == 'known':
                            known += 1
    
                        if colour_array.count(colour_array[index]) == 1:
                            colour_array[index] = 'known'
                            known+=1
    
                        if another_count > 1:
                            index2 = value_array.index(values[index])
    
                            if colour_array.count(colour_array[index2]) == 1:
                                colour_array[index2] = 'known'
                                known+=1
    
                            another_count -= 2
    
    
            if value_hint==4:
                for the_value in values:
                    if the_value not in hint_list:
                        another_count = value_array.count(the_value)
                        for i in range(value_array.count(the_value)):
    
                            index=value_array.index(the_value)
                            value_array[index]='known'
    
                            if colour_array[index]=='known':
                                known+=1
    
                            if colour_array.count(colour_array[index]) == 1:
                                colour_array[index] = 'known'
                                known+=1
    
                            if another_count > 1:
                                index2=value_array.index(the_value)
    
                                if colour_array.count(colour_array[index2])==1:
                                    colour_array[index2]='known'
                                    known+=1
    
                                another_count-=2
    
    
    
    
                value_hint+=1
    
            count=0
    
            for the_colour in colours:
                if the_colour in hint_list:
                    pass
                else:
                    if colour_array.count(the_colour)>count:
                        count=colour_array.count(the_colour)
                        index=colours.index(the_colour)
    
            if count!=0:
                    hints+=1
                    colour_hint+=1
                    hint_list.extend(colours[index])
                    another_count = colour_array.count(colours[index])
                    for i in range(another_count):
                        index = colour_array.index(colours[index])
                        colour_array[index] = 'known'
    
                        if value_array[index] == 'known':
                            known += 1
    
                        if value_array.count(value_array[index]) == 1:
                            value_array[index] = 'known'
                            known+=1
    
                        if another_count > 1:
    
                            index2 = colour_array.index(colours[index])
    
                            if value_array.count(value_array[index2]) == 1:
                                value_array[index2] = 'known'
                                known+=1
    
                            another_count -= 2
    
    
    
            if colour_hint==4:
                for the_colour in colours:
                    if the_colour not in hint_list:
                        another_count=colour_array.count(the_colour)
                        for i in range(another_count):
                            index=colour_array.index(the_colour)
                            colour_array[index]='known'
    
                            if value_array[index]=='known':
                                known+=1
    
                            if value_array.count(value_array[index]) == 1:
                                value_array[index] = 'known'
    
                                known+=1
    
                                if another_count > 1:
                                    index2 = colour_array.index(the_colour)
    
                                    if value_array.count(value_array[index2]) == 1:
                                        value_array[index] = 'known'
                                        known+=1
    
                                    another_count -= 2
    
                colour_hint+=1
    
        print (hints)
    
    
    
    