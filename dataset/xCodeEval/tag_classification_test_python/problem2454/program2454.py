def program2454():
    input()
    line = input().replace(')', '(').split('(')
    print(max([len(word) for subw in line[::2]  for word in subw.split('_')         ]),
          len([    word  for subw in line[1::2] for word in subw.split('_') if word ])
         )