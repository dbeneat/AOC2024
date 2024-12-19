#include <stdio.h>
#include <string.h>
#include <stdint.h>

char towels[500][10]={0};
int nbtowels=0;

uint64_t nbsolutions(char pattern[10], int start, uint64_t mem[100]){
    if(strlen(pattern+start)==0)return 1;
    if(mem[start])return mem[start]-1;
    uint64_t n=0;
    for(int i=0; i<nbtowels; i++){
        int k=strlen(towels[i]);
        if(strncmp(pattern+start,towels[i],k)==0){
            n+=nbsolutions(pattern,start+k,mem);
        }
    }
    mem[start]=n+1;
    return n;
}

int main(void){
    char line[3000];
    FILE*f=fopen("data/input19.txt","r");
    fgets(line,3000,f);
    char* tok = strtok(line,", \n");
    while(tok!=NULL){strcpy(towels[nbtowels],tok); nbtowels++;tok=strtok(NULL,", \n");}

    int part1=0;
    uint64_t part2=0;
    while(fgets(line,100,f)){
        if(line[0]!='\n'){
            int k=strlen(line);
            if(line[k-1]=='\n')line[k-1]='\0';
            uint64_t mem[100]={0};
            int64_t nbsol=nbsolutions(line,0,mem);
            part1+=(nbsol>0);
            part2+=nbsol;
        }
    }
    printf("%d %llu\n",part1,part2);
    return 0;
}