#include <stdio.h>
#define W 71
#define H 71

int G[H][W]={0};
int Q[1000]={0};
int read=0,write=0;
void resetQ(void){read=0;write=0;}
void enq(int x){Q[write]=x; write=(write+1)%1000;}
int deq(void){int x=Q[read]; read=(read+1)%1000; return x;}
int empty(void){return read==write;}

int main(void){
    FILE *f=fopen("data/input18.txt","r");
    int nobst=0,x=0,y=0;
    int Lobst[5000][2]={0};
    while(fscanf(f,"%d,%d",&x,&y)==2){
        G[y][x]=nobst+1; Lobst[nobst][0]=x; Lobst[nobst][1]=y;
        nobst++;
    }
    int solveFor(int k){
        int seen[H][W]={0};
        int sx=0,sy=0,ex=W-1,ey=H-1;
        resetQ();enq(0);enq(0);enq(0);
        while(!empty()){
            int d=deq(),x=deq(),y=deq();
            if(x==ex && y==ey)return d;
            if(seen[y][x])continue;
            seen[y][x]=1;
            if(x>0 && !(G[y][x-1]>0 && G[y][x-1]-1<=k)){enq(d+1);enq(x-1);enq(y);}
            if(x<W-1 && !(G[y][x+1]>0 && G[y][x+1]-1<=k)){enq(d+1);enq(x+1);enq(y);}
            if(y>0 && !(G[y-1][x]>0 && G[y-1][x]-1<=k)){enq(d+1);enq(x);enq(y-1);}
            if(y<H-1 && !(G[y+1][x]>0 && G[y+1][x]-1<=k)){enq(d+1);enq(x);enq(y+1);}
        }
        return 999999;
    }
    int part1=solveFor(1024);
    int left=1024,right=nobst;
    while(right-left>1){
        int middle=(left+right)/2;
        if(solveFor(middle)==999999){right=middle;}else{left=middle;}
    }
    printf("%d %d,%d\n",part1,Lobst[right][0],Lobst[right][1]);
    return 0;
}