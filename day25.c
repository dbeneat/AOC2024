#include <stdio.h>

int main(void){
    int part1=0;
    int codes[500][6]={0};
    int nc=0;
    char line[50];
    FILE *f=fopen("data/input25.txt","r");
    int n=0;
    while(fgets(line,50,f)){
        if(line[0]=='.' || line[0]=='#'){
            for(int i=0; i<5; i++){codes[nc][i]+=line[i]=='#';}
            n++;
        }
        if(n==7){
            n=0;
            if(line[0]=='#'){codes[nc][5]=1;}else{codes[nc][5]=0;}
            nc++;
        }
    }
    for(int i=0; i<nc;i++){
        for(int j=i; j<nc; j++){
            if(codes[i][5]==codes[j][5])continue;
            int a=1;
            for(int k=0;k<5;k++){if(codes[i][k]+codes[j][k]>7){a=0;break;}}
            part1+=a;
        }
    }
    printf("%d\n",part1);
    return 0;
}