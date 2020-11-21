//Questão: Notas e Moedas
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double nota;
    int resto, inteiro,inteiro1;

    cin >> nota;
    inteiro = nota;
    inteiro1 = nota*100;

    cout << "NOTAS:" << endl;
    cout <<(inteiro/100) << " nota(s) de R$ 100.00" <<endl;
    resto = inteiro%100;
    cout <<(resto/50) << " nota(s) de R$ 50.00" << endl;
    resto %= 50;
    cout << (resto/20) << " nota(s) de R$ 20.00" << endl;
    resto %= 20;
    cout << (resto/10) << " nota(s) de R$ 10.00" << endl;
    resto %= 10;
    cout << (resto/5) << " nota(s) de R$ 5.00" << endl;
    resto %= 5;
    cout << (resto/2) << " nota(s) de R$ 2.00" << endl;
    resto %= 2;

    cout << "MOEDAS:"<< endl;
    cout << resto/1 << " moeda(s) de R$ 1.00"<< endl;;
    
    inteiro1 = inteiro1%100;
    cout <<  inteiro1/50 << " moeda(s) de R$ 0.50"<< endl;;
    inteiro1 = inteiro1%50;
    cout <<  inteiro1/25 << " moeda(s) de R$ 0.25"<< endl;;
    inteiro1 = inteiro1%25;
    cout <<  inteiro1/10 << " moeda(s) de R$ 0.10"<< endl;;
    inteiro1 = inteiro1%10;
    cout <<  inteiro1/5 << " moeda(s) de R$ 0.05"<< endl;;
    inteiro1 = inteiro1%5;
    cout <<  inteiro1/1 << " moeda(s) de R$ 0.01"<< endl;;

    return 0;
}