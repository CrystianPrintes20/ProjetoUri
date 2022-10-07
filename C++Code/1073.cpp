//Questão: Quadrado de Pares
#include <iostream>
#include <math.h>

using namespace std;

int main(){

    int n,j;
    cin >> n;
  
    for(int i = 1; i < n+1; i++){
       
        if(i%2 == 0){
          j = pow(i,2);
          cout << i << "^2 = "<< j << endl;
        }
    }

    return 0;
}