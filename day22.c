#include <stdio.h>
#include <stdint.h>
#define MAX(a,b) (((a)>(b))?(a):(b))

unsigned int derive(unsigned int secret){
    secret=secret^(secret<<6);
    secret=secret%16777216;
    secret=secret^(secret>>5);
    secret=secret%16777216;
    secret=secret^(secret<<11);
    secret=secret%16777216;
    return secret;
}

int hash(int a, int b, int c, int d){
    int res=a;
    res=res*19+b;
    res=res*19+c;
    res=res*19+d;
    return res;
}

int prices[130321]={0};//130321=19^4
int main(void){
    uint64_t part1=0,part2=0;
    FILE *f=fopen("data/input22.txt","r");
    int m;
    while(fscanf(f,"%d",&m)==1){
        int k=4;
        int a=m;
        int b=derive(a);
        int c=derive(b);
        int d=derive(c);
        int e;
        int seen[130321]={0};
        while(k<=2000){
            e=derive(d);
            int d1=b%10-a%10+9,d2=c%10-b%10+9,d3=d%10-c%10+9,d4=e%10-d%10+9;
            int h=hash(d1,d2,d3,d4);
            if(seen[h]==0){
                prices[h]+=e%10;
                part2=MAX(part2,prices[h]);
                seen[h]=1;
            }
            a=b;b=c;c=d;d=e;
            k++;
        }
        part1+=e;
    }
    printf("%llu %llu\n",part1,part2);  
    return 0;
}