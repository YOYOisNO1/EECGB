def program1484():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    #define li long long int
    li n;
    li n2;
    
    li fun(li k){
        if(k <= 0ll) return -1;
        li ans = k;
        li n3 = n - k;
        n3 -= (li)(n3 * 0.1);
        while(n3 > 0){
            ans += max(min(k,n3),0ll);
            n3 = n3 - k;
            n3 -= (li)(n3 * 0.1);
        }
        return ans;
    }
    
    li binSearchMin(){
        li last = n-1;
        li first = 1;
        li mid = (last + first) / 2;
        while(last >= first){
            if(fun(mid) < n2)
                first = mid + 1;
            else if(fun(mid) > n2)
                last = mid - 1;
            else
                return mid;
            mid = (last + first) / 2;
        }
        if (fun(first) == n2){
            return first;
        }
        return last;
    }
    
    int main()
    {
        cin >> n;
        n2 = n / 2 + n % 2;
        li num = binSearchMin();
        while(fun(num) < n2){
            num ++;
        }
        cout << num;
        return 0;
    }