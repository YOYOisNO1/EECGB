def program1755():
    #include<iostream>
    #include<cstring>
    using namespace std;
    int main()
    {
    	string a,b;
    	int h1=0,h2=0,m1=0,m2=0,a1,a2;
    	bool flag=false;
    	cin>>a>>b;
    	for(int i=0;i<a.size();i++)
    		if(flag==false&&a[i]!=':')
    			h1*=10,h1+=(a[i]-48);
    		else if(a[i]==':')
    			flag=true;
    		else
    			m1*=10,m1+=(a[i]-48);
    	flag=false;
    	for(int i=0;i<a.size();i++)
    		if(flag==false&&b[i]!=':')
    			h2*=10,h2+=(b[i]-48);
    		else if(b[i]==':')
    			flag=true;
    		else
    			m2*=10,m2+=(b[i]-48);
    	if(m1<m2)
    		m1+=60,h1--;
    	if(h1<h2)
    		h1+=24;
    	a1=h1-h2;
    	a2=m1-m2;
    	if(a1<10)
    		cout<<0;
    	cout<<a1<<':';
    	if(a2<10)
    		cout<<0;
    	cout<<a2;		
    	return 0;
    }