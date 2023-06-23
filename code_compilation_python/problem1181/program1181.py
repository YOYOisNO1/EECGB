def program1181():
    #include <iostream>
    #include <vector>
    #define max(a,b) ((a) > (b) ? (a) : (b))
    using namespace std;
    int main()
    {
        int nb,nc,nw;
        cin >> nb >> nc >> nw;
        vector <int> v(nb);
        vector<int> :: iterator p,q;
        int a=0;
        for(int i=0;i<v.size();i++)
        {
            cin >> v[i];
        }
        for(int i=0;i<v.size();i++)
        {
            v.insert(v[i],nw);
            while(v.size()>2)
            {
                int len = v.size();
                for(int j=2;j<v.size();j++)
                {
                    if ((v[j - 2] == v[j - 1]) && (v[j - 1] == v[j]))
                    {
                        int c=j+1;
                        while(c<v.size())
                        {
                            if(v[j]!=v[c])
                            {
                                break;
                            }
                            c++;
                            p=v.begin()+j-2;
                            q=v.begin()+c;
                        }
                        v.erase(p-1,q);
                        break;
                    }
                }
                if (v.size() == len)
                {
                    break;
                }
            }
            a=max(a,nb-v.size());
        }
        cout << a << endl;
    }