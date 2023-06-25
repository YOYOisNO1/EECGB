def program1485():
    #include<bits/stdc++.h>
    using namespace std;
    
    int main(int argc, char const *argv[])
    {
    	string a, b; cin >> a >> b;
    	int num1 = 0, num2 = 0;
    	for (int i = 0; i < a.size(); i++) num1 += ((int)a[i] - 48) * pow(10, a.size() - i - 1);
    	for (int i = 0; i < b.size(); i++) num2 += ((int)b[i] - 48) * pow(10, b.size() - i - 1);
    	if (num1 > 99) num1++;
    	if (num2 > 99) num2++;
    	int sum = num1 + num2;
    	for (int i = 0; i < a.size(); i++) if (a[i] == '0') a.erase(a.begin() + i);
    	for (int i = 0; i < b.size(); i++) if (b[i] == '0') b.erase(b.begin() + i);
    	num1 = 0, num2 = 0;
    	for (int i = 0; i < a.size(); i++) num1 += ((int)a[i] - 48) * pow(10, a.size() - i - 1);
    	for (int i = 0; i < b.size(); i++) num2 += ((int)b[i] - 48) * pow(10, b.size() - i - 1);
    	stringstream os;
    	os << sum;
    	string s;
    	os >> s;
    	for (int i = 0; i < s.size(); i++) if (s[i] == '0') s.erase(s.begin() + i);
    	sum = 0;
    	for (int i = 0; i < s.size(); i++) sum += ((int)s[i] - 48) * pow(10, s.size() - i - 1);
    	if (num1 + num2 == sum) cout << "YES" << endl;
    	else cout << "NO" << endl;
    	return 0;
    }