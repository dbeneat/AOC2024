#include <stdio.h>
#include <stdint.h>

int64_t cost(int a, int b, int c, int d, int64_t e, int64_t f){
    int64_t N1=e*d-f*c,N2=a*f-b*e,D=a*d-b*c;
    if(N1%D==0 && N2%D==0){return 3*N1/D+N2/D;}else{return 0;}
}

int main(void){
    int64_t part1=0,part2=0;
    FILE *file=fopen("data/input13.txt","r");
    int a,b,c,d,e,f;
    int64_t B=10000000000000LL;
    while(fscanf(file,"Button A: X+%d, Y+%d\n",&a,&b)==2){
        fscanf(file,"Button B: X+%d, Y+%d\n",&c,&d);
        fscanf(file,"Prize: X=%d, Y=%d\n",&e,&f);
        part1+=cost(a,b,c,d,e,f);
        part2+=cost(a,b,c,d,e+B,f+B);
    }
    printf("%lld %lld\n",part1,part2);
    return 0;
}