def program2628():
    #include <iostream>
    #include <cmath>
     
    using namespace std;
    using ll_t = long long;
     
    int main()
    {
        ll_t x0,y0,ax,ay,bx,by,xs,ys,t;
        auto fx = [&](ll_t n)
        {
            long double an = powl(ax, n);
            return (long double)(an*x0*(ax - 1.) + (an - 1.)*bx) / (ax - 1.);
        };
     
        auto fy = [&](ll_t n)
        {
            long double an = powl(ay, n);
            return (long double)(an*y0*(ay - 1.) + an*by) / (ay - 1.);
        };
    
        auto f = [&](ll_t n)
        {
            ll_t txs = xs;
            ll_t tys = ys;
            ll_t tt = t;
            ll_t c = 0;
            for (ll_t i = n; i >= 0; i--)
            {
                ll_t ct = llabs(fx(i) - txs);
                ct += llabs(fy(i) - tys);
                if (tt < ct)
                    break;
                tt -= ct;
                c++;
                txs = fx(i);
                tys = fy(i);
            }
         
            for (ll_t i = n+1; true; i++)
            {
                ll_t ct = llabs(fx(i) - txs);
                ct += llabs(fy(i) - tys);
                if (tt < ct)
                    break;
                tt -= ct;
                c++;
                txs = fx(i);
                tys = fy(i);
            }
            return c;
        };
     
        cin >> x0 >> y0 >> ax >> ay >> bx >> by >> xs >> ys >> t;
        long double Nx = (logl(ax*xs + bx - xs) - logl(ax*x0 + bx - x0)) / logl(ax);
        long double Ny = (logl(ay*ys + by - ys) - logl(ay*y0 + by - y0)) / logl(ay);
        //cout << Nx << ' ' << Ny << '\n';
        Nx = Nx < 0 ? 0 : Nx;
        Ny = Ny < 0 ? 0 : Ny;
        long double minN = min(Nx, Ny);
        long double maxN = max(Nx, Ny);
        minN = floorl(minN);
        maxN = ceill(maxN);
        long long c = 0;
        for (; minN <= maxN; ++minN)
        {
            long long tmp = f(minN);
            c = max(c,tmp);
            //cout << minN << ' ' << tmp << '\n';
        }
        cout << c << '\n';
        return 0;
    }