//Questão: Teste de Seleção 1
#include <iostream>

using namespace std;

int main(){
    int a,b,c,d,somacd,somaab,par;
    cin >> a>>b>>c>>d;
    somaab = a+b;
    somacd = c+d;
    par = a%2;

    if (b > c && d > a && somacd > somaab && c >=0 && d >=0 && par==0){
        cout <<"Valores aceitos" << endl;
    }
    else{
        cout <<"Valores nao aceitos"<< endl;
    }
    return 0;
}