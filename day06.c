#include<stdio.h>

int main(void){
    char T[160][160];
    FILE *f=fopen("data/input06.txt","r");
    int N=0;
    while(fgets(T[N],160,f)){N++;}
    int startx=0,starty=0;
    for(int y=0; y<N; y++){
        for(int x=0; x<N; x++){
            if(T[y][x]=='^'){startx=x; starty=y;}
        }
    }
    int walk(int ispart1){
        int x=startx,y=starty,dx=0,dy=-1;
        int steps=0;
        while(1){
            if(ispart1){T[y][x]='*';}
            int nx=x+dx,ny=y+dy;
            if(nx<0||nx>=N||ny<0||ny>=N){return 0;}
            if(steps>7000){return 1;}
            if(T[ny][nx]=='#'){int temp=dx;dx=-dy;dy=temp;}else{x=nx;y=ny;steps++;}
        }
    }
    int part1=0,part2=0;
    walk(1);
    for(int y=0; y<N; y++){
        for(int x=0; x<N; x++){
            if(T[y][x]=='*' && (x!=startx || y!=starty)){
                part1++; 
                T[y][x]='#'; part2+=walk(0); T[y][x]='.';
            }
        }
    }
    printf("%d %d\n",part1,part2);
    return 0;
}