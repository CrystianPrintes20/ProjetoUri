//Questão: Idade em dias
#include <iostream>

using namespace std;

int main(){
    int n,resto,ano,mes,dia;
    cin >> n;
    ano = n/365;
    resto = n%365;
    mes = resto/30;
    dia = resto%30;
    cout << ano <<" ano(s)" << endl;
    cout << mes <<" mes(es)"<< endl;
    cout << dia <<" dia(s)"<< endl;
    return 0;

}