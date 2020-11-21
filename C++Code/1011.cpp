//Questão: Esfera
#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main(){
    double r;
    cin >> r;
    cout << fixed << setprecision(3) << "VOLUME = "<< (4/3.0)*3.14159*pow(r,3) << endl;

    return 0;
}