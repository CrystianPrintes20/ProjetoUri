//Questão: calculo Simples
#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main() {
    int cod1,cod2,npeca1,npeca2;
    double valor1,valor2;
    cout << fixed << setprecision(2);
    cin >> cod1 >> npeca1 >> valor1;
    cout << fixed << setprecision(2);
    cin >> cod2 >> npeca2 >> valor2;
    cout << fixed << setprecision(2);
    cout << "VALOR A PAGAR: R$ "<< (npeca1*valor1) + (npeca2*valor2) << endl;

    return 0;
}