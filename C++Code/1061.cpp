//Questão: Tempo de um Evento
#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
    int di = 0, hi = 0, mi = 0, si = 0, df = 0, hf = 0, mf = 0, sf = 0;
    char dia[4];
    char ponto[3];
    char diaf[4];
    char pontof[3];
    
    cin.get(dia,4) >> di >> hi;
    cin.get(ponto, 3) >> mi;
    cin.get(ponto, 3) >> si;

    cin.getline(dia,0);

    cin.get(diaf,4) >> df >> hf;
    cin.get(pontof, 3)>> mf;
    cin.get(pontof, 3) >> sf;
    
    long dura = (df*86400 + hf*3600 + mf*60 + sf) - (di*86400 + hi*3600 + mi*60 + si);
    cout << dura/86400 << " dia(s)\n";
    cout << (dura%86400)/3600 << " hora(s)\n";
    cout << ((dura%86400)%3600)/60 << " minuto(s)\n";
    cout << ((dura%86400)%3600)%60 << " segundo(s)\n";
    
    return 0;
}