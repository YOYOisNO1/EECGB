    n,k = map(int,input().split());
    cnt = map(int,input().split());
    cnt.sort();
    #cnt.reverse();
    
    available = 2*n;
    for i in xrange(k):
        x = min(available,cnt[i]/2);
        cnt[i] -= 2*x;
        available -= x;
    
    r = n;
    for i in xrange(k):
        x = min(r,cnt[i]/4);
        r -= x;
        cnt[i] -= 4*x;
    
def work(need,available):
        x = min(need,available);
        need -= x;
        available -= x;
        return need,available;
    
    if sum(map(lambda x:x >= 4,cnt)) != 0: print("NO");
    else:
        one = sum(map(lambda x:x == 1,cnt));
        two = sum(map(lambda x:x == 2,cnt));
        three = sum(map(lambda x: x == 3, cnt));
        if (two or three) and available: assert False;
        one,available = work(one,available);
        three,r = work(three,r);
        #print(one,two,three)
        #print(r,available)
        if three : print("NO");
        else:
            three = min(one,two);
            one -= three;
            two -= three;
            three,r = work(three,r);
            if three: print("NO");
            else:
                if one and two: assert False;
                #print(one,two;)
                #print(r,available)
                if two:
                    x = min(two,r);
                    two -= x;
                    r -= x;
                    if 2*two <= x: two = 0;
                two += (one + 1)/2;
                two,r = work(two,r);
                if two: print("NO");
                else: print("YES");
    