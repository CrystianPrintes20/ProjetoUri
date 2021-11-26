//Questão: Lanche
#include <iostream>
#include <iomanip>
 
 using namespace std;

 int main(){
     int cod, qtde;
     double valor;
     cin >> cod >> qtde;
      if (cod == 1){
        valor = 4 * qtde;
      }
      else if (cod == 2)
      {
          valor = 4.5 * qtde;
      }
      else if (cod == 3)
      {
          valor = 5 * qtde;
      }
      else if (cod == 4)
      {
          valor = 2 * qtde;
      }
      else if (cod == 5)
      {
          valor = 1.5 * qtde;
      }
      
      cout << fixed << setprecision(2) << "Total: R$ "<< valor << endl;
      
    return 0;
 }