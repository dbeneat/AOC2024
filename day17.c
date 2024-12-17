#include <stdio.h>
#include <stdint.h>

int main(void){
    FILE *f=fopen("data/input17.txt","r");
    uint64_t R[3];
    int prog[50]={0}, res[50]={0};
    fscanf(f,"Register A: %d Register B: %d Register C: %d Program:",R,R+1,R+2);
    int a;
    int len=0;
    while(fscanf(f,"%d,",&a)==1){prog[len]=a;len++;}

    int exec(){
        int ip=0;
        int lenres=0;
        while(ip<len){
            uint64_t op1=prog[ip],op2=prog[ip+1];
            uint64_t comb= op2<=3?op2:R[op2-4];
            switch(op1){
                case 0: R[0]=R[0]/(1ULL<<comb); break;
                case 1: R[1]=op2^R[1]; break;
                case 2: R[1]=comb%8; break;
                case 3: if(R[0]){ip=op2;continue;}; break;
                case 4: R[1]=R[1]^R[2]; break;
                case 5: res[lenres]=comb%8; lenres++; break;
                case 6: R[1]=R[0]/(1ULL<<comb); break;
                case 7: R[2]=R[0]/(1ULL<<comb); break;
            }
            ip+=2;
        }
        return lenres;
    }

    int lenres=exec();
    for(int i=0; i<lenres; i++){printf("%d",res[i]);}//Partie 1

    uint64_t searchDigit(int pos, uint64_t start, uint64_t step){
        if(pos<0)return start;
        for(int i=0; i<8; i++){
            R[0]=start+i*step,R[1]=0,R[2]=0;
            exec();
            if(prog[pos]==res[pos]){
                uint64_t s=searchDigit(pos-1, start+i*step, step/8);
                if(s!=0)return s;
            }
        }
        return 0;
    }
    uint64_t start=1ULL<<(3*(len-1));
    uint64_t blocksize=start;
    printf(" %llu\n",searchDigit(len-1,start,blocksize));
    return 0;
}