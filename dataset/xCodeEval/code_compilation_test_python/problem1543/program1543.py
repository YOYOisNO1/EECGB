def program1543():
    #include<stdio.h>
    int line(int x,int y){
    if (x==0&&y>0) return 2;
    if (x==0&&y<0) return 4;
    if (y==0&&x>0) return 1;
    if (y==0&&x<0) return 3;
    }
    char bolge(int x,int y){
    char *a="I",*b[2]="II",*c[3]="III",*d[2]="IV";
    if (x>0&&y>0) return a;
    if (x<0&&y>0) return b;
    if (x<0&&y<0) return c;
    if (x>0&&y<0) return d*;
    }
    int turn(char A, char B){
    if (A=='I' && B=='II') printf("RIGHT");
    if (A=='III' && B=='IV') printf("RIGHT");
    if (A=='I' && B=='IV') printf("LEFT");
    if (A=='III' && B=='II') printf("LEFT");
    if (A=='II' && B=='I') printf("LEFT");
    if (A=='IV' && B=='III') printf("LEFT");
    if (A=='IV' && B=='I') printf("RIGHT");
    if (A=='II' && B=='III') printf("RIGHT");
    }
    int main(){
    int i,a,b;
    char A,B;
    double x[3],y[3];
    for(i=0;i<3;i++){
    scanf("%lf %lf",&x[i], &y[i]);
    }
    for(i=0;i<3;i++){
    x[i]-=x[1];
    y[i]-=y[1];
    }
    if((x[2]/x[0])==(y[2]/y[0]){ printf("TOWARDS"); return 0;}
    if(x[0]==0||x[2]==0||y[0]==0||y[2]==0){
    a=line(x[0],y[0]);
    b=line(x[2],y[2]);
    if (a==1&&b==2) printf("RIGHT");
    if (a==2&&b==3) printf("RIGHT");
    if (a==3&&b==4) printf("RIGHT");
    else printf("LEFT");
    return 0;
    }
    A=bolge(x[0],y[0]);
    B=bolge(x[2],y[2]);
    turn(A,B);
    return 0;}