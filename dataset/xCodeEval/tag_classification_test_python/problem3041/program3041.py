def program3041():
    seq,text,count=int(input()),input(),0
    print([text[i]==text[i+1] for i in range(seq-1)].count(True))