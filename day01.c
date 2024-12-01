#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int cmpint(const void*a,const void*b){return *(int*)a-*(int*)b;}

int main(void){
    int A[1000], B[1000];
    uint64_t part1=0, part2=0;
    FILE *f=fopen("data/input01.txt","r");
    int N=0;
    while(fscanf(f,"%d %d",A+N, B+N)==2){N++;}
    qsort(A, N, sizeof(int),cmpint);
    qsort(B, N, sizeof(int),cmpint);
    for(int i=0; i<N; i++){
        part1+=abs(A[i]-B[i]);
        for(int j=0; j<N; j++){
            if(A[i]==B[j]){part2+=A[i];}
        }    
    }
    printf("%llu %llu\n",part1,part2);
    return 0;
}