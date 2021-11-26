//Questão: Formula de bhaskara
#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main(){
    double a,b,c,d,delta,delta1;
    cin >> a>>b>>c;
    delta = (pow(b,2)-4*a*c);
    if (a != 0 && delta > 0){
        delta1 = pow(delta,0.5);
        cout << fixed << setprecision(5)<< "R1 = "<< (-b + delta1) / (2 * a) << endl;
        cout << fixed << setprecision(5)<< "R2 = "<< (-b - delta1) / (2 * a) << endl;
    }
    else{
        cout <<"Impossivel calcular"<< endl;
    }
    return 0;
}