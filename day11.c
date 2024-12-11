#include <stdio.h>
#include <stdint.h>

struct {uint64_t key; uint64_t val;} cache[2000]={0};

int nbdigits(uint64_t n){
    uint64_t p=1; int i=0;
    while(p<=n){i++;p*=10;}
    return i;
}

uint64_t F(uint64_t n, int depth){
    if(depth==0) return 1;
    uint64_t hash=(101*n+7*depth)%2000;
    if(cache[hash].key==100*n+depth)return cache[hash].val;
    uint64_t res;
    if(n==0){res=F(1,depth-1);}
    else{
        int k=nbdigits(n);
        if(k%2==0){
            uint64_t p=1;
            for(int i=0; i<k/2; i++){p*=10;}
            uint64_t a=n/p, b=n%p;
            res=F(a,depth-1)+F(b,depth-1);
        }
        else{res=F(2024*n,depth-1);}
    }
    cache[hash].key=100*n+depth;
    cache[hash].val=res;
    return res;
}

int main(void){
    FILE *f=fopen("data/input11.txt","r");
    uint64_t part1=0, part2=0; int n;
    while(fscanf(f,"%d",&n)==1){part1+=F(n,25);part2+=F(n,75);}
    printf("%llu %llu\n",part1,part2);
    return 0;
}