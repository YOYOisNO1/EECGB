    #include <stdio.h>
    #include <algorithm>
    using namespace std;
    
    int hp_y, atk_y, def_y;
    int hp_m, atk_m, def_m;
int hp,atk, def;
    int minn = 1e8;
    int main()
    {
    	scanf("%d%d%d", &hp_y, &atk_y, &def_y);
    	scanf("%d%d%d", &hp_m, &atk_m, &def_m);
	scanf("%d%d%d", &hp, &atk, &def);
    	int i, j, z;
        
    	for(i = 0; i <= 100; i++)
    	{
    		for(j = 0; j <= 100; j++)
    		{
    			int a1 = atk_y;
    			int b1 = def_y;
    			a1  += i;
    			b1  += j;
    
    			int dec_y = max(atk_m - b1, 0);
    			int dec_m = max(a1 - def_m, 0);
    
    			if(dec_m == 0)
    				continue;
    			else
    			{
    				if(dec_y == 0)
					minn = min(minn, i * atk + j * def);
    				else
    				{
    					for(z = 0; z <= 500; z++)
    					{
    						int c1 = hp_y;
    						c1 += z;
    						
    						
    						double a = c1 * 1.0 / dec_y;
    						double b = hp_m * 1.0 / dec_m;
    						int a2 = (int)a;
    						if(a2 != a)
    							a2 = a2 + 1;
    						int b2 = (int)b;
    						if(b2 != b)
    							b2 = b2 + 1;
    						if(a2> b2)
							minn = min(minn, i * atk + j * def + z * hp); 
    					}
    				}
    			}
    		}
    	}
    	printf("%d\n", minn);
    }