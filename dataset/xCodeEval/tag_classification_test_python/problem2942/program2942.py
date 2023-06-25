def program2942():
    don_vi={'0':"zero",'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine"}
    chuc={'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
    chuc1={'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
    s=input()
    if(len(s)==1):
        print(don_vi[s])
    else:
        if(s[0]=='1'):
            print(chuc1[s])
        elif(s[1]=='0'):
            print(chuc[s[0]])
        else:
            print(chuc[s[0]]+'-'+don_vi[s[1]])