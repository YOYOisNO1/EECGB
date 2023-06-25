def program2442():
    import re
    l = input()
    s = input()
    bat = []
    for i in re.findall('\((.*?)\)', s):
        bat.extend([j for j in i.split('_') if j != ''])
    
    cat = [len(i )for i in re.sub('\((.*?)\)','_', s).split('_')]
    print(max(cat),) len(bat)