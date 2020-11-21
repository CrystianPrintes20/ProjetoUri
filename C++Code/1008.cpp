//Questão: Salario
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
   int N, HT;
   cin >> N >> HT;
   float SH;
   cin >> SH;
   cout << "NUMBER = "<< N <<endl;
   cout << fixed << setprecision(2);
   cout << "SALARY = U$ "<< HT*SH <<endl;
   return 0;

}