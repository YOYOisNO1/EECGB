    
def inRange(x):
        return ( (0<x) and (x<1000000000));
    
def getSum(x):
        s=str(x);
        sm=0;
        for i in range(len(s)):
            sm+=int( s[i] );
        return sm;
    
    if( __name__ == '__main__'):
        a,b,c=map( long , str(input()).split() );
        st=set([]);
    
        for sm in range(1,100):
            x=b*pow(sm,a)+c;
    
            if( inRange(x)):
                if( getSum(x) == sm):
                    st.add(x);
    
        ans=sorted( list(st));
        print( len(ans));
        for i in range( len(ans)):
            print(ans[i]),