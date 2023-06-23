def program1542():
    #include <iostream>
    #include <cmath>
    using namespace std;
    
    int main()
    {
        int a1,a2,b1,b2,c1,c2;
        cin >> a1 >> a2;
        cin >> b1 >> b2;
        int v1 = a1-b1;
        int v2 = a2-b2;
        cin >> c1 >> c2;
        int u1 = c1-b1;
        int u2 = c2-b2;
        if(fabs(v1) > 1000 and fabs(v2) > 1000 and fabs(u1) > 1000 and fabs(u2) > 1000)
        {
        v1 = ceil(v1/2000);
        v2 = ceil(v2/2000);
        u1 = ceil(u1/2000);
        u2 = ceil(u2/2000);
        }
        long long int parcel1 = v1*u2;
        long long int parcel2 = v2*u1;
    
        if(parcel1 == parcel2)
        cout << "TOWARDS" << endl;
        if(parcel1 > parcel2)
        cout << "RIGHT" << endl;
        if(parcel1 < parcel2)
        cout << "LEFT" << endl;
    
    //    cout << v1 << " " << v2 << endl;
    //    cout << u1 << " " << u2 << endl;
    //    cout << aux;
        return 0;
    }
    
    //47715 -171800
    //
    //-228153 -358383
    //
    //-414736 -82515