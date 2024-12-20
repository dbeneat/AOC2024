#include <stdio.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

int N=0;
int abs(int x){return x>0?x:-x;}
int hash(int x,int y){return N*y+x;}
int main(void){
    FILE *f=fopen("data/input20.txt","r");
    char G[150][150];
    int dist[150*150]={0};
    while(fgets(G[N],150,f)&&G[N][0]!='\n'){N++;}
    int sx,sy,ex,ey;
    for(int y=0;y<N;y++){
        for(int x=0;x<N;x++){
            if(G[y][x]=='S'){sx=x;sy=y;}
            if(G[y][x]=='E'){ex=x;ey=y;}
        }
    }

    int x=sx,y=sy,d=0;
    while(1){
        if(G[y][x]=='#')continue;
        dist[hash(x,y)]=d+1;
        if(x==ex && y==ey)break;
        d++;
        if(x>0 && G[y][x-1]!='#' && dist[hash(x-1,y)]==0)x--;
        else if(x<N-1 && G[y][x+1]!='#' && dist[hash(x+1,y)]==0)x++;
        else if(y>0 && G[y-1][x]!='#' && dist[hash(x,y-1)]==0)y--;
        else if(y<N-1 && G[y+1][x]!='#' && dist[hash(x,y+1)]==0)y++;
    }

    int part1=0,part2=0;
    int D=dist[hash(ex,ey)]-1;
    for(int y=1; y<N-1; y++){
        for(int x=1; x<N-1; x++){
            if(G[y][x]=='#')continue;
            int d1=dist[hash(x,y)]-1;
            for(int yy=MAX(1,y-20);yy<MIN(N-1,y+21);yy++){
                for(int xx=MAX(1,x-20);xx<MIN(N-1,x+21);xx++){
                    if(G[yy][xx]=='#')continue;
                    int d2=dist[hash(ex,ey)]-dist[hash(xx,yy)];
                    int d3=abs(x-xx)+abs(y-yy);
                    if(d3<=20){
                        int d=d1+d2+d3;
                        if(d3==2 && d<=D-100)part1++;
                        if(d<=D-100)part2++;
                    }
                }
            }
        }        
    }
    printf("%d %d\n",part1,part2);
    return 0;
}