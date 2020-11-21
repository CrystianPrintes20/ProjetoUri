//Questão: Salario com Bonus
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
   string NOME;
   float SALARIO, TOTALV, TOTAL;
   cin >> NOME;
   cout << fixed << setprecision(2);
   cin >> SALARIO >> TOTALV;
   cout << fixed << setprecision(2);
   cout << "TOTAL = R$ "<<((TOTALV*15)/100) + SALARIO <<endl;
   return 0;

}