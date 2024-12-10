#include <stdio.h>

int main(void){
    char line[100];
    FILE *f=fopen("data/input08.txt","r");
    int grid[100][100]={0};
    int ant[500][3];
    int nant=0;
    int W=0,H=0;
    int part1=0,part2=0;
    while(fgets(line,100,f) && line[0]!='\n'){
        W=0; while(line[W]!='\n' && line[W]!='\0'){
            if(line[W]!='.'){
                ant[nant][0]=line[W];
                ant[nant][1]=W;
                ant[nant][2]=H;
                nant++;
            }
            W++;
        }
        H++;
    }
    int inside(int x,int y){return x>=0 && x<W && y>=0 && y<H;}
    for(int i1=0; i1<nant;i1++){
         for(int i2=0; i2<nant;i2++){
            if(i1!=i2 && ant[i1][0]==ant[i2][0]){
                int x1=ant[i1][1],x2=ant[i2][1];
                int y1=ant[i1][2],y2=ant[i2][2];
                int dx=x2-x1,dy=y2-y1;
                int k=0;
                while(inside(x2+k*dx,y2+k*dy)){
                        if(k==1){grid[y2+k*dy][x2+k*dx]=1;}
                        else{
                            if(grid[y2+k*dy][x2+k*dx]==0){
                                grid[y2+k*dy][x2+k*dx]=2;
                            }
                        }
                    k++;
                }
            }
        }   
    }
    for(int y=0; y<H; y++){
        for(int x=0; x<W; x++){
            if(grid[y][x]==1){part1++;part2++;}
            else if(grid[y][x]==2){part2++;}
        }
    }
    printf("%d %d\n",part1,part2);
    return 0;
}