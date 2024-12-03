#include <stdio.h>
int i=0;
char E[5000];
int num(int k, int *res){
    *res = 0;
    char c=E[i];
    if(c<'0'||c>'9') return 0;
    while(c>='0' && c<='9'){
        *res=10*(*res)+c-'0'; i++; c=E[i];
    }
    return 1;
}

int main(void){
    int part1=0, part2=0;
    FILE *f=fopen("data/input03.txt","r");
    while(fgets(E,5000,f)){
        i=0;
        char a;
        int op1,op2;
        while(E[i]!='\0'){
            if(E[i++]=='m')
            if(E[i++]=='u')
            if(E[i++]=='l')
            if(E[i++]=='(')
            if(num(i,&op1))
            if(E[i++]==',')
            if(num(i,&op2))
            if(E[i++]==')')
                part1+=op1*op2;
            
        }
    }
    
    printf("%d %d\n",part1,part2);
    return 0;
}