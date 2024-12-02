#include <stdio.h>
int remap(int i,int skip){return i>=skip?i+1:i;}

int main(void){
    int part1=0, part2=0; char line[100]; int L[8];
    FILE *f=fopen("data/input02.txt","r");
    while(fgets(line,100,f)){
        int N=sscanf(line,"%d %d %d %d %d %d %d %d",L,L+1,L+2,L+3,L+4,L+5,L+6,L+7);
        int ok(int skip){
            for(int i=0; i<(skip==999?N-1:N-2); i++){
                int e1=L[remap(1,skip)]-L[remap(0,skip)];
                int e2=L[remap(i+1,skip)]-L[remap(i,skip)];
                if(e1*e2<=0 || e2*e2>9){ return 0; }
            }
            return 1;
        }
        part1+=ok(999);
        for(int skip=0; skip<N; skip++){
            if(ok(skip)){part2++; break;}
        }
    }
    printf("%d %d\n",part1,part2);
}