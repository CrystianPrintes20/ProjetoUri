//Questão: Tempo de jogo
#include <iostream>

using namespace std;

int main(){
    int hi,hf,tt;
    cin >> hi >> hf;

    if(hi == hf){
        printf("O JOGO DUROU 24 HORA(S)\n");
    }
    else if (hi > hf)
    {
        hf += 24;
        tt = hf -hi;
        printf("O JOGO DUROU %d HORA(S)\n", tt);
    }
    else
    {
        tt = hf - hi;
        printf("O JOGO DUROU %d HORA(S)\n", tt);
    }
    
    
}