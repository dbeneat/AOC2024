#include <stdio.h>

int main(void){
    char line[100];
    FILE *f=fopen("data/input10.txt","r");
    int G[50][50]={0};
    int W=0,H=0;
    while(fgets(line,100,f) && line[0]!='\n'){
        W=0;
        while(line[W]!='\n' && line[W]!='\0'){G[H][W]=line[W]-'0';W++;}
        H++;
    }
    int inside(int x,int y){return x>=0 && x<W && y>=0 && y<H;}
    int score(int x,int y,int code){
        if(code && G[y][x]/10==code){return 0;}else{G[y][x]=10*code+G[y][x]%10;}
        if(G[y][x]%10==9)return 1;
        int total=0;
        if(inside(x-1,y) && G[y][x-1]%10==G[y][x]%10+1)total+=score(x-1,y,code);
        if(inside(x+1,y) && G[y][x+1]%10==G[y][x]%10+1)total+=score(x+1,y,code);
        if(inside(x,y-1) && G[y-1][x]%10==G[y][x]%10+1)total+=score(x,y-1,code);
        if(inside(x,y+1) && G[y+1][x]%10==G[y][x]%10+1)total+=score(x,y+1,code);
        return total;
    }
    int part1=0,part2=0;
    for(int y=0; y<H; y++){
        for(int x=0; x<W; x++){
            if(G[y][x]==0){
                int code=10*(50*y+x+1);
                part1+=score(x,y,code);
                part2+=score(x,y,0);
            }
        }
    }
    printf("%d %d\n",part1,part2);
    return 0;
}