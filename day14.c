#include <stdio.h>
#define MAXROBOTS 500

int main(void){
    #define W 101
    #define H 103
    int R[MAXROBOTS][4]={0};
    int nbr=0;
    FILE *f=fopen("data/input14.txt","r");
    int x,y,vx,vy;
    while(fscanf(f,"p=%d,%d v=%d,%d\n",R[nbr],R[nbr]+1,R[nbr]+2,R[nbr]+3)==4){
        nbr++;}
    void update(int r[4]){r[0]=(r[0]+r[2]+W)%W; r[1]=(r[1]+r[3]+H)%H;}
    int Hres=0,Vres=0;
    for(int i=0;i<100;i++){
        int LH[W]={0}, LV[H]={0};
        for(int r=0;r<nbr;r++){
            LH[R[r][0]]++; LV[R[r][1]]++;
            if(LH[R[r][0]]>20)Hres=i;
            if(LV[R[r][1]]>20)Vres=i;
            update(R[r]);
        }
    }
    int a=0,b=0,c=0,d=0;
    for(int i=0; i<nbr; i++){
        int x=R[i][0],y=R[i][1];
        if(x<(W-1)/2 && y<(H-1)/2)a++;
        if(x<(W-1)/2 && y>(H-1)/2)b++;
        if(x>(W-1)/2 && y<(H-1)/2)c++;
        if(x>(W-1)/2 && y>(H-1)/2)d++;
    }
    int part1=a*b*c*d;
    int part2;
    for(int i=0; i<W*H;i++){
        if(i%W==Hres && i%H==Vres){part2=i;break;}
    }
    printf("%d %d\n",part1,part2);
    return 0;
}