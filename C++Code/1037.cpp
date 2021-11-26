//Questão: Intervalo
#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main(){
    double a;
    cin >> a;
    if (a >= 0 && a <= 25.0000){
        cout << "Intervalo [0,25]" << endl;
    }
    else if (a > 25.0000 && a <= 50.0000)
    {
       cout << "Intervalo (25,50]" << endl;
    }
    else if (a > 50.0000 && a <= 75.000)
    {
        cout << "Intervalo (50,75]" << endl;
    }
    else if (a > 75.0000 && a <= 100.0000)
    {
        cout << "Intervalo (75,100]" << endl;
    }
    else
    {
        cout << "Fora de intervalo" << endl;
    }
    
    
    return 0;
}