def program2912():
    // #include<Mr.Unknown>
    #include<iostream>
    #include<queue>
    #include<cmath>
    #include<set>
    #include<algorithm>
    #include<vector>
    #include<map>
    #include<cstring>
    using namespace std;
     
    // #define int long long
    #define ll long long
     
    #define f(i,a,b) for (int i=a;i<=b;i++)
    #define ii pair<int,int>
    #define llll pair<ll,ll>
    #define iii pair<pair<int,int>, int>
     
    #define pb push_back
     
    const ll MOD = 1000000007;
    // const ll mod = 998244353;
     
    const int N = 200005;
    
    ll n, m, k ;
    ll a[N] ;
    
    void pre_init() {
        
    }
     
    void init() {
        
    }
    
    
    void MrUnknown() {
        if (n > m) swap(n,m);
        sort(a+1,a+1+k) ;
        ll tong = 0 ;
        int num2 = 0, num3 = 0;
        f(i,1,k) {
            ll x = a[i]/n;
            if (x >=2 ) tong += x;
            // cout << i << " " << tong << "|1\n" ;
            if (x == 2) num2++;
            if (x>2) num3++;
            if (tong >= m) {
                cout << "Yes\n" ;
                return;
            }
            if (tong+1==m) {
                if (i==k) {
                    break;
                }
                ll y = a[k]/n ;
                if (tong - x + y >= m) {
                    cout << "Yes\n" ;
                    return;
                }
                if (num3 > 0) {
                    cout << "Yes\n" ;
                    return ;
                }
                if (num2 > 0 && y > 2) {
                    cout << "Yes\n" ;
                    return ;
                }
                break;
                // cout << "No\n" ;
                // return;
            }
        }
        swap(n,m) ;
        tong = 0;
        num2 = num3 = 0 ;
        f(i,1,k) {
            ll x = a[i]/n;
            if (x >=2 ) tong += x;
            // cout << i << " " << tong << "|2\n" ;
            if (x == 2) num2++;
            if (x>2) num3++;
            if (tong >= m) {
                cout << "Yes\n" ;
                return;
            }
            if (tong+1==m) {
                if (i==k) {
                    break;
                }
                ll y = a[k]/n ;
                if (tong - x + y >= m) {
                    cout << "Yes\n" ;
                    return;
                }
                if (num3 > 0) {
                    cout << "Yes\n" ;
                    return ;
                }
                if (num2 > 0 && y > 2) {
                    cout << "Yes\n" ;
                    return ;
                }
                break;
                // cout << "No\n" ;
                // return;
            }
        }
        cout << "No\n" ;
    }
     
    void inp() {
        // Case++;
        
        cin >> n >> m >> k ;
        f(i,1,k) cin >> a[i] ;
        
        pre_init();
        
        MrUnknown();
     
        init();
        
    }
     
    signed main() // watch toaru pls :)
    {
        ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
     
        // freopen("intput.txt","r",stdin);
        // freopen("output.txt","w",stdout);
     
        // ------------------------------------- init -------------------------------
     
        int t; cin>>t; while(t--) 
            inp();
     
    }
    /*
    1
    4
    ((((
     
     
    */
     
    //---------------------------------------------------------------------------------------------------------------------------------------
     
    /*
    MMMMMMMMMMMMMMMMMMMMMMMMN0xdxO00Odx0d,',,,'.',:xKK00000000000xdk00OdxOxk0000000000000000000000OkkO0000000000OO000000000000Od;'''',:ccccllc::lc:cOWMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMWX0OkO0000Odlol;,',,''.;oOXK00000000000OddO00Odx0xx00000000000000000000000kxk0000000000OOO00000000000KKkc,'''':ccll:::cl::ld0WMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMXOkO0K000Oxo;,;;;;;,,';o0XXK000000000000kox000kox0xx00000000000000000000000Oxdk00000000000kkO000000000KXXKxc,''';ooc;,;lo:;lloKMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMN0k0KK000Oxl;;;::;::;,:dOXXK00000000000000dok000kod0kxO00000000000000000000000OddO00000000000kdk00000000KXNXK0d:''';c:;;:lc:c::cdNMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMXOOKXK00Oxl;;;::;;:;,,lOKKKK00KXXK00000000OooO000Ooo0Odx00000000000000000000000Okdk000000000000xdxO000KKKKKXXXXKOl,''',:cc;;cdl;clOWMMMMMMMMMMM
    MMMMMMMMMMMMMMMWKO0XXK00ko:;:::,,;:;';d0KKK00KXXNXK00000000kldO000OooO0xdO000000000OO000000O00000OddO00OO00000000xoxO0KXXXXKKKKKK00x:''';::;;loc:c:dNMMMMMMMMMMM
    MMMMMMMMMMMMMMWKOKXXK0Oxc;;::;',;:;,ck0000O0KXXNNXKKKK00000xlx00000dlx0kdk000000000OO00000OO00000Oxok00OO000000000xox0XXNNNXK0000000kc''',:lc::lol:lKMMMMMMMMMMM
    MMMMMMMMMMMMMWK0KXXXKOo;;::;,',::;;oO000OO0KXXNNNXKKXK0O000dlx00000kloO0xdO00000000Ok00000OO000000kod00Ok00KKKK00K0dlx0XNNNXX0OO00000Ol''';cc::odlcl0MMMMMMMMMMM
    MMMMMMMMMMMMWKOKXXXKkc;;c:,'';c:;:d0000OOO00KXXXXKKXXKOOKX0olk0000OOolk0Odx00000000OkO0000OO000000OooO0OkOKXXXX00KXOolkKXXXKK00kO00000Ol,'',clclllcoKMMMMMMMMMMM
    MMMMMMMMMMMMKOKKKKOo:;::;,'';c:;:x0000OO000000K000KXK0O0KXKolkKKK0OOkloO0xdk0000000OkO0000OOO000KK0dlkK0kk0XXXX0O0XKxcoOKKK0000Okk00000Ol,'';c:,:lcdNMMMMMMMMMMM
    MMMMMMMMMMMXO0K0Odc;:::,'',:c;;:x0OO0OkO0000000000000Ok0KKOolxKXXOk00dcd00xdO0KK0000kk00000OOKKKKXKxcdKKkxOKXNXKOOKKOocdO0000000Oxk000OOOl'..';;::c0MMMMMMMMMMMM
    MMMMMMMMMMW0O00kl;;:c;,'',:c;,:x0OO0OkO00000000OO0000kk000klcx0XKkk0X0ocxKKxx0XXKKKKOk0KXXKOOKXKKXXkclOKOdx0XXXKkk000xccx00000000kxO000OOkc..,cllckWMMMMMMMMMMMM
    MMMMMMMMMMKO00xc;:c:;,'',::;,:dOOO0Okk000000000OO000Oxk00OxccdOK0xx0XXklckX0dxKXNXXX0kOXNNXOkKXKKXXOc:xOOddO0000kxO00Oo:lk0000000OxxO00OkOk:,coddxKWMMMMMMMMMMMM
    MMMMMMMMMNOOOo;;:c:;,,,;c:;,;oOOk0Oxk000000000OkO000kxO00kl:cdk0Odd0XX0xlcx0OdkXNNNXKkkKXNX0k0XKKXXOc;lkOxdxO000OxxO00xccdO0000000kdx000OkOdc:cllo0WMMMMMMMMMMMM
    MMMMMMMMMKkxl;;cc;;;;;:c:;;;lOOkO0kxO000000000kxO00OxxO0Od:':oxOkodOKK00dccdOkdkKKXXKOxOXXXKkOK00K0k:':okkodk000Oxdk00Oo:lx0000000Oxdk00OkkOo::ccl0MMMMMMMMMMMMM
    MMMMMMMMWOo:,;c:;;;;;:c:;;,ckOkO0OdxO00000000Oxk000kdx00xl,.;lxOkllk0000xolcoOkdoxO000kxO0KKxxO00OOx:.'cdkdoxO00OkodOOOxc:oO0000000OdxO00kxOxc:;':KMMMMMMMMMMMMM
    MMMMMMMMXo;;;c:;;;;;:c;;;,:dOkk0Odok0000OO000Oxk00Odlx0Od;;;;cdkxlcxOOOOkdooclxkxddO00OdxO0OxxOO0OOx:'';lxxooxO00kdoxOOko:cxO000000Oxdk00Oxkkc;;.;OMMMMMMMMMMMMM
    MMMMMMMM0:,;cc;;;;;:c;;;,,oOkxO0kodO000OOOO00kdk00klcx0xc;ll;:oxxc:okOOOkdoxxocodxddkO0xdkOOxdkO0OOx:;c;;odolokO0OxooxOOxc:oO0000000kdxO0OxxOl'.';kWMMMMMMMMMMMM
    MMMMMMMWO:,;:;,,,,:c;,;,,:kOxk0OdlxOO00OOOO0Oxdk00xcckOd::dd:;ldd:;cxkkOkdldkOxlclodoxOOddOOkdxOOOOd;:do;:odlcokOOxocokOkl:cxO000000Odok0OddOd,.',oNMMMMMMMMMMMM
    MMMMMMMWkc;,,'''',:;'',',dOxdk0kolkOOOOOOOOOOxdk0Oo:cxkl:lxxl;:oo:,:oxkkkxllxOOOkxllllokkddOOdoxkkxo;;ll:,:ll::oxxxoccokko::dO000000Odlx0Odlkk:.',c0MMMMMMMMMMMM
    MMMMMMMNx,.......,;,''',lOOdxO0xlokOOOOOkOOOOdok0kc;cxxccdxxdc;loc',cdddxxoclxO00Okxolccododxocldxdc;:lllc;:cc;:ldddl:cdxd:;lxkOO00OOxldOOdlxk:.'':kWMMMMMMMMMMM
    MMMMMMMNo.........'...,:dOxdkOOdcokOOOOkkOOOkookOd;'cdo::olll:,:lc,,;coodxdl:lxOOOOOOkxooolcdxolxkdccdxxxxdccl:,:oxxdc;cxxl;cxOOOOOO0kloOOdlxk:.'';oKMMMMMMMMMMM
    MMMMMMMNd'.............ckOddkOkocdkOOOOkkOOOkolxxl'':lc::lllooc;cl::::oddxxoc:okOOOOOOOkkxdooxxloxoclxxxxxxdlcc,':oddl;,lxo;;dO00OOOOkllkOdldx;''',cOWMMMMMMMMMM
    MMMMMMMNkllc,'........'oOkdxOOklcokOOOkxxkkkdccdd:,,:lcldxxxxxdc:lcco:cododdl::oxkOOOOOOOkdxdlxdlllcoxxdoddddl:;,,:looc;;lo:;okOOOOOOkolkkdcoo,.''';dXMMMMMMMMMM
    MMMMMMMWkoO0Oxl;'.....;xOxoxOOklcoxOOkkdxkkkx::oo:::;lclxxxxdddl::ccdoccooodol::coxkOOOOOkddxoldocccoddxxxxkxxo:;;::colc::c:;lkOOOOOOkolxko:lc,...',cOWMMMMMMMMM
    MMMMMMMMOok000Od:,,,..ckkooxOOklcoxOOOkxxkOkd;,ll:ll:cclddddddddl:cclxocllloooc:;:oxkOOOOkxodo::lccoxkkkkkkkxkxdc;clcclcclc;;lxOOOOOOkolxxl:c:'....';dXMMMMMMMMM
    MMMMMMMMKdx00Oko;:c:,,lOxloxOOkocodkkkkxdkkkd;'cc:oo::coxxxxxxxkxoc:codolllloooc:;:lxkOOOkxooo:;cccdkkkkkkxxxxxxdl:lolcccldc;cxOOOOOOxllxxc;c;.......,xWMMMMMMMM
    MMMMMMMMXdd00Okl;cc;,;dkoclxOOkocldkkkkxdxkkd,';:cdxl:coxxxxxxkkkxdccoxxdlllloollc;;ldkkkkkdlo:;:ccldxxdolc::;;;;;;;:cc:;;ldlcxOOOOkOxlldd:;:,........cKMMMMMMMM
    MMMMMMMMWkoO0Ox:;c:;,:dx:;lxOkkdcloxkkkxdxkkd:,;:lddo::odddddddddxxdccdkkxolllllllc,,codkkkdolc;:cll:::,'.................';;:odxkkkOdcldl;;;'........lXMMMMMMMM
    MMMMMMMMM0ox0Ol,:c;;,:xd,'cxkkkxlcodkkkkddxkd:::,cool;,;,,,,,;;::clooccdxkxolclllllc,;:lodxxoc::;;:;...',;:::::::,,;;,'......':oxkkkko:lo:,;,........lKMMMMMMMMM
    MMMMMMMMMXddOk:,c:;;,:dl'.:dkkkkocldxkkkxddkdc:;',,,'..............,;;,:oxkkdl:cllllc:ccclodol;,,',;;:oxkkkkxkkkkxddOOkxo,..':xkkkkkkl:lc:;'.........lXMMMMMMMMM
    MMMMMMMMMWOokd;;c:;;,:dc'.,oxkkkdccodkkkxdodd:,'.......''';:ccccc:;,,'..;okkkxo:;:cllcldolclol:,:dkdoxkkkkxkkkOOOOOdx0KOo'';;lxkkkkkxc:c:oo,........',xWMMMMMMMM
    MMMMMMMMMMXdoc':c;;;,:o:'''cxkkkxl:ldxkxdoc;;'....',:oxxooxkkkkkkkkkkxdc;ldkkOkxolcllcclxkdolc::lxkxxxxxddddxddddddlcodo::llcokkkkkkd::::xx;....'''''';kWMMMMMMM
    MMMMMMMMMMWOc,'::;;;,:l:''';okkkxo::ldxxddoc:;'.'lxO0K0xdkOOkkxxkkxkkkkxdxkkOOOOOOxdxxdooxO0Oxdodk000000OOOOOkkkxxdodooddxxdodkxxkkkl;;;cxx;..''''''''':OWMMMMMM
    MMMMMMMMMMMXo',:;,;;;:c;,'''cxkkxo:,:oxxddxdll:',:lxOOkoldddddddxxkkOOOOOOOO000000K00KKKKKXXXXXXKXXXXK0KXXKKKKKKKK0000OOOOOxdxkxxkkxc,:ookx,.'''''''''',cOWMMMMM
    MMMMMMMMMMMWd';:,,;;;cc;,''';okkxd:''coxdodxlcc:cc:cooloodxkkkOOOOOOOO000KKKXXXXXNNNNNNNNNNNNNNNNNNNNKOkKXXXXXXXXXXXXXKKKKKkdxxxxkko;,lkkOo'.''''''''''',l0WMMMM
    MMMMMMMMMMMXl';;',;;:c:;,,';:cdkkdc'.,cddolddccclxxxkdlcokOOOOOOO00KKKXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXOdkKXXXXXXXXXXK0KXXKxxxxxxkxc::oO0x;..''..........,c0WMMM
    MMMMMMMMMMM0:,:;',;;::,,,,,::,cxkxc'.';coolldo::cdkOOo,',lkO000KKXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXNXOdx0XXXXXXXXXKO0KKkdxxxxkkololx0x;..'ol............lXMMM
    MMMMMMMMMMMk,,:,'',;c:'',,;c:',lxxl,.,cccolclol:;cdOkc''';xKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX00KKKK0kOKXXXXXXXKOxkdldxdxkkdlloxOx;...cKO;.........,lOWMMM
    MMMMMMMMMMNd';:,'',;c:,',;:c;'',oxo;.;ol;:llccolc:cdx:''',dKXXXXXXXXXNNNNNNNNNNNNNNXXNNNNNNNNNNNNNNNXOkkkk0K0O0XXK0OOkkxdloddxxkxlcdkkl'..',c0Xl......,lxKWMMMMM
    MMMMMMMMMMXl';;'''';c:,'',:c;''';ld:.,oo;';cc::lllddc,''''oKXXXXXXXNNNNNNNNNNNNNNNNKKNNNNNNNNNNNNNNNNNKkxOxdO0xxOK0kO00Oxodddxxkxlokd;''''',:kNk,...'oKWMMMMMMMM
    MMMMMMMMMM0:';;'''';c:,,,,:c;,'',:lc',ld:..':c;:ccoo;'''',oKXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXKkoodoldOkdxkxdoddxxkkxlcdl,'''''';dXKc...,xNMMMMMMMMM
    MMMMMMMMMMXxdxd;...,;,,,,,:c;;,,:;';,,ldc''..,:cclc;''''',xXXXXXNNNNNNNNNNNNNNNNNNNNNNNWNNNNNNNNNNNNNNNNNNKOxoc:::cl::::ldddxxkxxldXXo'...'',cONd'.',c0MMMMMMMMM
    MMMMMMMMMMMMMMK:........'',;,,,,,'...'cdc,''..'ccll;''''.:OXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNWWWWWWNWNNNNNNNNNNOollc:;;,;;;coodxxxxddd0WMO;......,oXXo;'';dNMMMMMMMM
    MMMMMMMMMMMMMMO;......................:dl,'''.'lkx:''''''lKXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWWNNNNNNXXNNNXXX0d:;;;,,,,:oodxxxxolddOWMXc.......lXMWKkollkWMMMMMMM
    MMMMMMMMMMMMMM0:.....................,cdo;''''.,dkc''''',xXNNNNNNNNNNNNNNNWNNNNWWWNWWNNNNNNNXXKK000Ok0XNNXXXXXOo;,,,,:ooodxxkxdoodkNMWd'....;dXMMMMMMNKXWMMMMMMM
    MMMMMMMMMMMMMMWXOxxdo:'';;;;;;;,'...';ldd:'''''.,c;''''.;xXNNNNNNNNNNNNXOO0KKKKKKKKKKKKKXKKKKKKK00KKXNNNNNK0O0K0d:,,;odooxxkxxK0ddxKMMO,..;xXWMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMXdcdOOOkOOkoc;,:lcodl,'''''..'''''.,dXNNNNNNNNNNNNNXKKK00KXXNNNWWWWWWWWNXXXXXNNWNNNNNNXKkxdl;,;ldoodxkkxONNkdd0WMKc.'cKMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMKolk00OOOOxl::loccodc''''''..''''''lKNNNNNNNNNNNNNNNNNXKK000Okk0KKK0000KXNNWNNNNNNX0O0XXOl:,,lkxooxkkxxKMM0xdkNMWk:',kWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMNd;ok00OkOkoldoclccodc,'''''.'''''.:ONNNNNNNNNWNNWNWWNXKK00kdclk00KKKXNNNNWWWNXXNNNK0O0XX0o;ckOdldkkkdkNMMXxokXMMWXOdONMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMNd:coO00kxxdx0xcc:lkxdc'''''..''''.,dXNNNNNWWNNNXKKKKKKKXNNX0k0NNNNNWWWWWWWWWWNNNNNK00kxdxocx0koldkkxo0MMMNdlxKMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMNdcccdO00xloOKOo:;lKXkoc''''..'''''.:0NNWWNNXK000KKXNNNNX00OOKNWWWWWWWWWWWWWWWWNNNNXKKXOl;;oO0xlldkkddXMMMNoco0WMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMKoclccx00klckXX0d:l0MNOo:''''.'''''.'oXWWXK00KXNWWNXK0OOkO0KNWWWWWWWWWWWWWWWWWWNWNXX0O0x:,ckOOxlldkxoxNMMMXo;lOWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMOllllcok00o:oOKXKOdOWMWKo,'''.''''''.'lkxlckNWWNX0kkkO0KNNNWWWWWWWWWWWWWWWWWWWWWWNNNNKxoddxOkOklldxxlxWMMMKc;:kWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMNdclllccdO0kc:ldkO00OOKNWKl'''.''''''...'''';okOkxxOKXNNWWWWWWWWWWWWWWWWWWWWWWWWWWNX0OO0NNOkOxkOocoxdlkWMMWk:;;xWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMWOlllllcclk0Odl:::oxO00kOXWKc'''''''''''''''''..,lk0KXNWWWWWWWWWWWWWWWWWWWWWWWWWNX0kxokWMMKkOOdx0dcldocxNMMKo:;;xWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMW0ollllccccx0Odll:;;cok00OONM0:''''''''''''''''...':okKNWWWWWWWWWWWWWWWWWWWWWWNX0kxddddKMMMKxOkldOklcoocoXMNxc;,;kMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMW0xdolllccccoOOdll:;:::lx00OKMW0c'''''''''''''''......';cx0KNNWWWWWWWWWWWWWWNKOkxddxxxdxKMMMKxOxclk0xllollOXxlc;,cKMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMW0OOxllllcclcoOOdlc:;clddokOkXMMMKo,'''''''''''''''.......'cdxkOO0XNNWWWNNK0OxddxxxxxxxddKMMMXkkOocdO0dcllcclllc;;dNMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMN0O0OdollccclcoOkolc;:lxK0odkKWMMMMNx;'''''''''''''''.......,oxxddddxkkkxxxdddxxxxxxxxxxolxNMMW0xOxllxO0xccc;;llc:lKMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMN0000kdlllccllcdOxolc:cd0XxlxXWMMMMMMWOc''''''''''''''........:dxxxxxxxddddxxxxxxxdddolc:,:xk0NWW0xxdllxO0xcc:;:lclOWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMN0000OkdllcclollkOdllodxxxxx0NMMMMMMMMMWKo,'''''''''''''.......';:::ccldxxxdlc:c:::;;,,'''''o0xx0KXKOxocldk0kl:;,;cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMN00K00OxolccoollxOxodOOkkxOXWMMMMMMMMMMMMMNx;''''''''''''.........''''':dO0Oxc'''''''''''''.,kW0OXXKKK0Odccok0Odc;,dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMN00K00OkdlccodooxOkokX0k0k0MMMMMMMMMMMMMMMMMWO:';ccc:;,''''........''''';loool:'''''''''',,,:OWMXkKMMWXKKK0xoox00ko::kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMWK0K00Okxlccooook0OdkWKkO0kKMMMMMMMMMMMMMMMMWN0kook000kxl:;'.....';::::;;:c::::::::::ccclcccxXWMMNxOMMMMMNXK0dclxO00kl:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMN0KK00Oxlclddodk00OOXWOk00k0WMMMMMMMMMMMMMWXKKXWNkox000K00kdlc::;:ldddddoolcccloooooooooloxKWMMMMWxxWMMMMMMMN0xllxO00OxoONMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMX0K00Oxl:oxxddk000O0NNkk00kkNMMMMMMMMMMMWX0KNMMMMNdlk00000000OOkkoclllloodoooloddoododddkKWMMMMMMWxkWMMMMMMMMMXdlox0000OkKWMMMMMMMMMMMMMMMMMMMMMMMMMM
     
    */