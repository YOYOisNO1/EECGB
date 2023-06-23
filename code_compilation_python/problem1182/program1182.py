def program1182():
    #include <iostream>
    #include <cstring>
    #include <cassert>
    #include <vector>
    #include <queue>
    #include <list>
    #include <utility>
    #include <cstdio>
    #include <algorithm>
    using namespace std;
    
    vector<int> colors;
    int x;
    
    /*int norm(list<int>& c) {
      int removed = 0;
      bool changed;
      do {
        changed = false;
        if (c.size() < 3)
          return removed;
        int run_len = 1;
        list<int>::iterator last = c.begin();
        list<int>::iterator it = next(c.begin());
        list<int>::iterator begin_it = last;
        for (; it != c.end(); last = it, it++) {
          if (*it == *last) {
            run_len++;
          } else {
            if (run_len >= 3) {
              c.erase(begin_it, next(it));
              removed += run_len;
              changed = true;
            }
            run_len = 1;
            begin_it = it;
          }
        }
    
        if (run_len >= 3) {
          c.erase(begin_it, c.end());
          removed += run_len;
          changed = true;
        }
      } while (changed);
      return removed;
    }
    
    int maxdestroy_at(vector<int>&c, int pos) {
      list<int> tmp;
      for (int i = 0; i < c.size(); i++) {
        if (i == pos) {
          tmp.push_back(x);
        }
        tmp.push_back(c[i]);
      }
      return norm(tmp);
    }
    
    int maxdestroy(vector<int>& c) {
      if (c.empty()) return 0;
    
      int m = (x == c[0]) ? maxdestroy_at(c, 0) : 0;
      for (int i = 1; i < c.size(); i++) {
        if (c[i] == x && c[i - 1] == c[i]) {
          m = max(m, maxdestroy_at(c, i));
        }
      }
      return m;
    }*/
    
    void compact_in_place(vector<pair<int, int> >& c) {
      // filter the zeroes
      vector<pair<int, int> > new_c;
      for (int i = 0; i < c.size(); i++) {
        if (c[i].second) new_c.push_back(c[i]);
      }
      c = new_c;
    
      bool cow = false;
      for (int i = 1; i < c.size(); i++) {
        if (c[i].first == c[i - 1].first) {
          c[i - 1].second += c[i].second;
          c[i].second = 0;
          cow = true;
        }
      }
      if (cow) {
        // filter the zeroes
        vector<pair<int, int> > new_c;
        for (int i = 0; i < c.size(); i++) {
          if (c[i].second) {
            new_c.push_back(c[i]);
          }
        }
        c = new_c;
      }
    }
    
    int combine(vector<pair<int, int> >& c) {
      compact_in_place(c);
    
      int destroyed = 0;
      for (int i = 1; i < c.size(); i++) {
        if (c[i].second >= 3) {
          destroyed += c[i].second;
          c[i].second = 0;
        }
      }
      if (destroyed) {
        return destroyed + combine(c);
      }
      return destroyed;
    }
    
    int maxdestroy(const vector<pair<int, int> >& c) {
      int md = 0;
      for (int i = 0; i < c.size(); i++) {
        if (c[i].first == x) {
          vector<pair<int, int> > aux = c;
          if (aux[i].second + 1 == 3) {
            aux[i].second++;
            int change = combine(aux) - 1;
            md = max(md, change);
          }
        }
      }
      return md;
    }
    
    int maxdestroy(const vector<int>& c) {
      if (c.empty()) return 0;
    
      vector<pair<int, int> > compact;
      compact.push_back(make_pair(-1, 1));
      int color = c[0];
      int length = 1;
      for (int i = 1; i < c.size(); i++) {
        if (c[i] == color) {
          length++;
        } else {
          compact.push_back(make_pair(color, length));
          color = c[i];
          length = 1;
        }
      }
      compact.push_back(make_pair(color, length));
    
      return maxdestroy(compact);
    }
    
    int main() {
      int n, k;
      scanf("%d %d %d", &n, &k, &x);
    
      for (int i = 0; i < n; i++) {
        int p;
        scanf("%d", &p);
        colors.push_back(p);
      }
      printf("%d\n", maxdestroy(colors));
      return 0;
    }
    
    
    