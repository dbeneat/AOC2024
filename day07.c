#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int main(void){
    uint64_t part1=0,part2=0;
    char line[100];
    uint64_t L[50]={0};
    uint64_t correct(uint64_t res,uint64_t last,uint64_t ispart2){
        uint64_t pow=10;
        if(ispart2){while(pow<=L[last]){pow*=10;}}
        if(last==1){return res==L[1];}
        return (res>=L[last] && correct(res-L[last],last-1,ispart2))
        ||(res%L[last]==0 && correct(res/L[last],last-1,ispart2))
        ||(ispart2 && res%pow==L[last] && correct(res/pow,last-1,ispart2));
    }
    FILE *f=fopen("data/input07.txt","r");
    while(fgets(line,100,f)){
        int N=0;
        char* tok = strtok(line,": ");
        while(tok!=NULL){L[N]=strtoull(tok,NULL,10);N++;tok=strtok(NULL,": ");}
        if(correct(L[0],N-1,0))part1+=L[0];
        if(correct(L[0],N-1,1))part2+=L[0];
    }
    printf("%llu %llu\n",part1,part2);
    return 0;
}