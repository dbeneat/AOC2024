#include <stdio.h>

typedef struct E{
    int prio;
    int data;}E;

E PQ[1000];
int pqsize=0;

void printPQ(){
    for(int i=0; i<pqsize; i++){printf("(%d|%d)\n",PQ[i].prio,PQ[i].data);}
    printf("\n");
}

void insert(int pr,int x){
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


int main(void){
    insert(1,10);
    insert(5,11);
    insert(3,15);
    insert(90,100);
    insert(10,20);
    printPQ();
    printf("\n");
    extractMin();
    printPQ();

    return 0;
}