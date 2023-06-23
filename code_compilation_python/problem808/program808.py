def program808():
    #include <iostream>
    #include <cstdio>
    #include <vector>
    #include <list>
    #include <complex>
    #include <algorithm>
    #include <set>
    #include <map>
    #include <queue>
    #include <string>
    #include <cstring>
    #include <stack>
    #include <cmath>
    #include <iomanip>
    #include <sstream>
    #include <cassert>
    #include <numeric>
    #include <cfloat>
    #include <climits>
    
    
    using namespace std;
    typedef long long ll;
    typedef ll li;
    typedef pair<int,int> PI;
    #define EPS (1e-6)
    #define rep(i,n) for(int i=0;i<(int)(n);++i)
    #define REP(i, n) rep (i, n)
    #define F first
    #define S second
    #define mp(a,b) make_pair(a,b)
    #define pb(a) push_back(a)
    #define min3(a,b,c) min((a),min((b),(c)))
    #define min4(a,b,c,d) min((a),min3((b),(c),(d)))
    #define SZ(a) (int)((a).size())
    #define ALL(a) a.begin(),a.end()
    #define FLL(a,b) memset((a),b,sizeof(a))
    #define CLR(a) memset((a),0,sizeof(a))
    #define FOR(it,a) for(__typeof(a.begin())it=a.begin();it!=a.end();++it)
    #define FORR(it,a) for(__typeof(a.rbegin())it=a.rbegin();it!=a.rend();++it)
    
    template<typename T,typename U> ostream& operator<< (ostream& out, const pair<T,U>& val){return out << "(" << val.F << ", " << val.S << ")";}
    template<class T> ostream& operator<< (ostream& out, const vector<T>& val){out << "{";rep(i,SZ(val)) out << (i?", ":"") << val[i];return out << "}";}
    typedef double FP;
    typedef complex<FP> pt;
    typedef pt P;
    typedef pair<pt,pt> line;
    namespace std{
      bool operator<(const P&a,const P&b){
        if(abs(a.real()-b.real())>EPS)
          return a.real()<b.real();
        return a.imag()<b.imag();
      }
    }
    FP dot(P a,P b){return real(conj(a)*b);}
    FP crs(P a,P b){return imag(conj(a)*b);}
    P ortho(P a){return P(imag(a),-real(a));}
    P ortho(line a){return ortho(a.S-a.F);}
    P crspt(P a,P b,P c,P d){b-=a,d-=c;return a+b*crs(d,c-a)/crs(d,b);}
    P crspt(line a,line b){return crspt(a.F,a.S,b.F,b.S);}
    bool onl(P a1,P a2,P b){return abs(b-a1)+abs(b-a2)<abs(a1-a2)+EPS;}
    bool onl(line a,P b){return onl(a.F,a.S,b);}
    bool iscrs(line a,line b){P c=crspt(a,b);return onl(a,c)&&onl(b,c);}
    void pkuassert(bool t){t=1/t;};
    int dx[]={0,1,0,-1,1,1,-1,-1};
    int dy[]={1,0,-1,0,-1,1,1,-1};
    enum{TOP,BTM,LFT,RGT,FRT,BCK};
    int dxdy2ce[]={RGT,FRT,LFT,BCK};
    int s2i(string& a){stringstream ss(a);int r;ss>>r;return r;}
    template<class T> T shift(T a,int b,int c,int d,int e){
      __typeof(a[0])t=a[b];
      a[b]=a[c];a[c]=a[d];a[d]=a[e];a[e]=t;return a;}
    template<class T> T rgt(T a){return shift(a,TOP,LFT,BTM,RGT);}
    template<class T> T lft(T a){return shift(a,TOP,RGT,BTM,LFT);}
    template<class T> T frt(T a){return shift(a,TOP,BCK,BTM,FRT);}
    template<class T> T bck(T a){return shift(a,TOP,FRT,BTM,BCK);}
    line mkl(P a,P v){return line(a,a+v);}
    FP lpdist(line a,P b){return abs(b-crspt(a,mkl(b,ortho(a))));}
    FP spdist(line a,P b){
      P c(crspt(a,mkl(b,ortho(a))));
      return onl(a,c)?abs(b-c):min(abs(a.F-b),abs(a.S-b));
    }
    FP ssdist(line a,line b){
      return
        iscrs(a,b)?0.:
        min4(spdist(a,b.F),spdist(a,b.S),
             spdist(b,a.F),spdist(b,a.S));
    }
    
    bool ok(string a){
      FOR(it,a)
        if(!islower(*it) && !isupper(*it) &&
           !isdigit(*it) && *it!='_')
          return false;
      return true;
    }
    
    string solve(){
      string no="NO";
      string in;
      getline(cin,in);
      
      if(in.find('@') == string::npos)
        return no;
      
      int atp = in.find('@');
      string username = in.substr(0,atp);
      in = in.substr(atp+1);
      
      if(in.find('/') == string::npos) in += "/a";
    
      atp = in.find('/');
      string host = in.substr(0,atp);
      in = in.substr(atp+1);
    
      // cout << username << endl;
      // cout << host << endl;
      
      if(SZ(username)<1 || 16<SZ(username))
        return no;
      if(SZ(in)<1 || 16<SZ(in))
        return no;  
      if(SZ(host)<1 || 32<SZ(host))
        return no;
    
      if(!ok(username)) return no;
      if(!ok(in)) return no;
      in = host;
      
      while(in!=""){
        string a;
        if(in.find('.') == string::npos){
          a = in;
          in = "";
        }else{
          a = in.substr(0,in.find('.'));
          in = in.substr(in.find('.')+1);
        }
        if(SZ(a)<1 || 16<SZ(a))
          return no;
        if(!ok(a))
          return no;
      }
      
      return "YES";
    }
    
    int main(int argc, char *argv[])
    {
      cout << solve() << endl;
      return 0;
    }