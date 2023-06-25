def program1537():
    colour, instructions = input(), input()
    
    position = 1
    
    for i in instructions:
      if i == colour[position-1]:
        position += 1
    
    print(position)