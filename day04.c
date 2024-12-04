#include <stdio.h>

int main(void){
    int part1=0, part2=0, N=0;
    char T[150][150];
    FILE *f = fopen("data/input04.txt","r");
    while(fgets(T[N],150,f)){ N++; }
  
    int C(int i,int j,char c){return i>=0 && i<N && j>=0 && j<N && T[i][j]==c;}
    int XMAS(int i, int j, int di, int dj){
        return C(i,j,'X') && C(i+di,j+dj,'M') && C(i+2*di,j+2*dj,'A') && C(i+3*di,j+3*dj,'S');
    }
    int MAS(int i, int j, int di, int dj){
        int r1 = C(i-di,j-dj,'M') && C(i,j,'A') && C(i+di,j+dj,'S');
        int r2 = C(i+di,j+dj,'M') && C(i,j,'A') && C(i-di,j-dj,'S');
        return r1||r2;
    }

    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            for(int di=-1; di<=1; di++){
                for(int dj=-1; dj<=1; dj++){
                    part1+=XMAS(i,j,di,dj);
                }
            }
            part2+=MAS(i,j,1,1) && MAS(i,j,-1,1);
        }
    }
    printf("%d %d\n",part1,part2);
    return 0;
}