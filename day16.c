#include <stdio.h>

typedef struct E{
    int prio;
    int data;}E;

E PQ[50000];
int pqsize=0;

void printPQ(){
    for(int i=0; i<pqsize; i++){printf("(%d|%d)\n",PQ[i].prio,PQ[i].data);}
    printf("\n");
}

void insert(int pr,int x){
    if(pqsize==50000){printf("ERREUR\n");return;}
    PQ[pqsize].prio=pr;
    PQ[pqsize].data=x;
    int i1=pqsize;
    int i2=(i1-1)/2;
    while(PQ[i1].prio<PQ[i2].prio){
        E temp=PQ[i1];
        PQ[i1]=PQ[i2];
        PQ[i2]=temp;
        i1=i2;
        i2=(i1-1)/2;
    }
    pqsize++;
}

E extractMin(void){
    E res=PQ[0];
    PQ[0]=PQ[pqsize-1];
    int i1=0;
    pqsize--;
    while(1){
        int i2=2*i1+1;
        int i3=2*i1+2;
        int min=i1;
        if(i2<pqsize && PQ[min].prio>PQ[i2].prio){min=i2;};
        if(i3<pqsize && PQ[min].prio>PQ[i3].prio){min=i3;};
        if(min==i1)break;
        E temp=PQ[i1];
        PQ[i1]=PQ[min];
        PQ[min]=temp;
        i1=min;
    }
    return res;
}

int N=0;
int hash(int x,int y,int h){return 4*(N*y+x)+h;}
int main(void){
    FILE *f=fopen("data/input16.txt","r");
    char G[150][150];
    int seen[90000]={0};
    int dist[90000]={0};
    int dx[4]={1,0,-1,0};
    int dy[4]={0,-1,0,1};
    while(fgets(G[N],150,f)&&G[N][0]!='\n'){N++;}

    for(int y=0;y<N;y++){
        for(int x=0;x<N;x++){
            if(G[y][x]=='#')continue;
            for(int h=0;h<4;h++){
                int code=hash(x,y,h);
                if(G[y][x]=='S' && h==0){insert(0,code);dist[code]=0;}
                else{insert(999999,code);dist[code]=999999;}
            }
        }
    }

    while(pqsize>0){
        E u=extractMin();
        int data=u.data;
        int h=data%4;
        int x=(data/4)%N;
        int y=(data/4)/N;
        if(x==N-2 && y==1){break;}
        if(seen[data])continue;
        seen[data]=1;
        for(int hh=0;hh<4; hh++){
            int nx=x+dx[hh],ny=y+dy[hh];
            if(G[ny][nx]=='#')continue;
            int code=hash(nx,ny,hh);
            if(seen[code])continue;
            int deltaD=1;
            if(hh!=h)deltaD=1001;
            int newD=u.prio+deltaD;
            if(newD<dist[code]){dist[code]=newD;insert(newD,code);}
        }
    }

    int part1=0;
    int h=0;
    for(h=0;h<4;h++){
        part1=dist[hash(N-2,1,h)];
        if(part1<999999){break;}
    }

    void explore(int x,int y,int h){
        if(G[y][x]=='#')return;
        G[y][x]='O';
        int d=dist[hash(x,y,h)];
        for(int hh=0;hh<4; hh++){
            if(dist[hash(x,y,hh)]==d){
                int nx=x-dx[hh],ny=y-dy[hh];
                for(int hhh=0;hhh<4;hhh++){
                    int dd=dist[hash(nx,ny,hhh)];
                    if(d-dd==1 ||d-dd==1001)explore(nx,ny,hhh);
                }
            }
        }
    }

    explore(N-2,1,h);
    int part2=0;
    for(int y=0;y<N;y++){
        for(int x=0;x<N;x++){
            if(G[y][x]=='O')part2++;
        }
    }
    printf("%d %d\n",part1,part2);
    return 0;
}