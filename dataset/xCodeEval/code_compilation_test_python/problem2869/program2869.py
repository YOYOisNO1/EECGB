def program2869():
    
    #include <map>
    #include <list>
    #include <iostream>
    using namespace std;
    
    typedef pair<int, string> Pair;
    
    bool cmp(const Pair& a, const Pair& b) {
       return (a.first != b.first ? a.first > b.first : a.second < b.second);
    }
    
    inline bool lucky(char c) { return c == '4' or c == '7'; }
    
    int main() {
       string S;
       cin >> S;
       const int N = S.size();
       map<string, int> count;
       for (int i = 0; i < N; i++) {
          if (lucky(S[i])) {
             string part;
             part += S[i];
             count[part]++;
             for (int j = i + 1; j < N; j++) {
                if (!lucky(S[j])) break;
                part += S[j];
                count[part]++;
             }
          }
       }
       if (count.empty()) {
          cout << -1 << endl;
       } else {
          list<Pair> L;
          map<string, int>::iterator it = count.begin();
          for (; it != count.end(); it++) {
             L.push_back(make_pair(it->second, it->first));
          }
          L.sort(cmp);
          
          cout << L.front().second << endl;
       }
    }
       