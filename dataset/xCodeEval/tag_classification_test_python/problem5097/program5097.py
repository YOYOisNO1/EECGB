def main():
        mode="filee"
        if mode=="file":f=open("test.txt","r")
        #f.readline()
        #input()
        get = lambda :[str(x) for x in (f.readline()[:-1] if mode=="file" else input()).split("|")]
        scale = get()
        q = input()
        if abs(len(scale[0]) - len(scale[1]))%2 != len(q)%2 or abs(len(scale[0]) - len(scale[1]))>len(q):
            print("Impossible")
            return
        if len(scale[0])<len(scale[1]):
            mid = len(scale[1])-len(scale[0])
            scale[0]+=q[:mid]
        else:
            mid = len(scale[0])-len(scale[1])
            scale[1]+=q[:mid]
        for z in range(mid,len(q),2):
            scale[1]+=q[z]
            scale[0]+=q[z+1]
        print("|".join(scale))
    
        if mode=="file":f.close()
    
    
    if __name__=="__main__":
        main()