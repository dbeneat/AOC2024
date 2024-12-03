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
    int part1=0, part2=0, ok=1;
    FILE *f=fopen("data/input03.txt","r");
    while(fgets(E,5000,f)){
        i=0;
        int op1,op2;
        while(E[i]!='\0'){
            switch(E[i++]){
                case 'm':
                    if(E[i++]=='u')
                    if(E[i++]=='l')
                    if(E[i++]=='(')
                    if(num(i,&op1))
                    if(E[i++]==',')
                    if(num(i,&op2))
                    if(E[i++]==')'){
                        part1+=op1*op2;
                        if(ok) part2+=op1*op2;
                    }  
                    break;
                case 'd':
                    if(E[i++]=='o'){
                        switch(E[i++]){
                            case '(':if(E[i++]==')') ok=1; break;
                            case 'n':
                                if(E[i++]=='\'')
                                if(E[i++]=='t')
                                if(E[i++]=='(')
                                if(E[i++]==')')
                                    ok=0;
                                break;
                        }
                    }
            }
        }
    }
    printf("%d %d\n",part1,part2);
    return 0;
}