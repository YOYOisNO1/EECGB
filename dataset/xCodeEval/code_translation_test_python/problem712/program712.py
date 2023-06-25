def program712():
    import math
    people, planesperperson, planespersheet, sheetsperpack = [int(i) for i in input().split(' ')]
    sheetsperperson = math.ceil(planesperperson / planespersheet)
    sheetstotal = sheetsperperson * people
    packstotal = math.ceil(sheetstotal / sheetsperpack)
    print(packstotal)