#include <stdio.h>
#define MAXCC 1000

int main(void){
    char G[150][150];
    FILE *f=fopen("data/input12.txt","r");
    int N=0;
    while(fgets(G[N],150,f) && G[N][0]!='\n'){N++;}
    int CC[150][150]={0};
    int numcc=1;
    void dfs(int x,int y){
        if(CC[y][x]>0)return;
        CC[y][x]=numcc;
        if(x>0 && G[y][x-1]==G[y][x])dfs(x-1,y);
        if(x<N-1 && G[y][x+1]==G[y][x])dfs(x+1,y);
        if(y>0 && G[y-1][x]==G[y][x])dfs(x,y-1);
        if(y<N-1 && G[y+1][x]==G[y][x])dfs(x,y+1);
    }
    for(int y=0; y<N; y++){
        for(int x=0; x<N; x++){
            if(CC[y][x]==0){dfs(x,y);numcc++;}
        }
    }
    int get(int x,int y){
        if(x<0||x>=N||y<0||y>=N)return -1;
        return CC[y][x];
    }
    int area[MAXCC]={0},perim[MAXCC]={0},corners[MAXCC]={0};
    for(int y=0; y<N; y++){
        for(int x=0; x<N; x++){
            for(int dy=-1; dy<=1; dy+=2){
                for(int dx=-1; dx<=1; dx+=2){
                    int a=get(x,y),b=get(x+dx,y),c=get(x,y+dy),d=get(x+dx,y+dy);
                    if((a!=b && a!=c)||(a==b && a==c && a!=d)){corners[a]++;}
                }
            }
            int k=4;
            int a=get(x,y),b=get(x-1,y),c=get(x,y-1);
            if(a==b)k-=2;
            if(a==c)k-=2;
            area[a]++; perim[a]+=k;
        }
    }
    int part1=0,part2=0;
    for(int i=0;i<MAXCC;i++){part1+=area[i]*perim[i]; part2+=area[i]*corners[i];}
    printf("%d %d\n",part1,part2);
    return 0;
}