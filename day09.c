#include <stdio.h>
#include <stdint.h>

typedef struct {int pos; int size;} E;

uint64_t arith(int start, int nb){return (2*start+nb-1)*nb/2;}
int main(void){
    char line[22000];
    E blocks[10000],voids[10000];
    FILE *f=fopen("data/input09.txt","r");
    fgets(line,22000,f);
    
    
    int firstBeforePos(int pos, int sz){
        for(int i=0; voids[i].pos<pos; i++){
            if(voids[i].size>=sz)return i;
        }
        return -1;
    }
    uint64_t solve(int ispart2){
        int pos=0;
        int nbblocks=0,nbvoids=0;
        for(int i=0;line[i]!='\n' && line[i]!='\0';i++){
            int x=line[i]-'0';
            if(i%2==0){blocks[nbblocks].pos=pos; blocks[nbblocks].size=x; nbblocks++;}
            else{voids[nbvoids].pos=pos; voids[nbvoids].size=x; nbvoids++;}
            pos+=x;
        }
        uint64_t res=0;
        int numbl=nbblocks-1;
        while(numbl>=0){
            E bl=blocks[numbl];
            if(bl.size==0){numbl--; continue;}
            int nb=ispart2?bl.size:1;
            int i=firstBeforePos(bl.pos,nb);
            blocks[numbl].size-=nb;
            if(i>=0 && i<nbvoids){
                res+=arith(voids[i].pos,nb)*numbl;
                voids[i].pos+=nb; voids[i].size-=nb;
            }
            else{res+=arith(bl.pos+bl.size-nb,nb)*numbl;}
        }
        return res;
    }
    uint64_t part1=solve(0);
    uint64_t part2=solve(1);
    printf("%llu %llu\n",part1,part2);
    return 0;
}