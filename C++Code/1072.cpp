//Questão: Intervalo 2
#include <iostream>

using namespace std;

int main(){

    int n, x, dentro = 0, fora = 0;
    cin >> n;
  
    for(int i = 0; i < n; i++){
        cin >> x;
        if(x >= 10 && x <= 20){
            dentro += 1;
        }else{
            fora += 1;
        }
    }

    cout << dentro << " in\n";
    cout << fora << " out\n";

    return 0;
}