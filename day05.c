#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    FILE *f=fopen("data/input05.txt","r");
    char L[100];
    int order[100][100]={0};
    while(fgets(L,100,f)){
        int a,b;
        if(sscanf(L,"%d|%d",&a,&b)!=2){break;}
        order[a][b]=1;
    }
    int part1=0,part2=0;
    while(fgets(L,100,f)){
        int N=0, line[50]={0};
        char* tok = strtok(L,",");
        while(tok!=NULL){line[N]=atoi(tok);N++;tok=strtok(NULL,",");}
        int ok=0,wasordered=1;
        while(!ok){
            ok=1;
            for(int i=0; i<N-1; i++){
                int a=line[i],b=line[i+1];
                if(order[b][a]){
                    ok=0; wasordered=0;
                    int temp=line[i]; line[i]=line[i+1]; line[i+1]=temp;
                }
            }
        }
        if(wasordered){part1+=line[N/2];}else{part2+=line[N/2];}
    }
    printf("%d %d\n",part1,part2);
    return 0;
}