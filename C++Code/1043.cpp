//Questão: Triângulo
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double a,b,c,P,A;
    cin >> a >> b >> c;
    if((a+b)>c && (b+c)>a && (c+a)>b){
        P = a + b + c;
        cout <<fixed<<setprecision(1)<< "Perimetro = "<<P<<endl;
    }
    else
    {
        A = ((a+b)*c)/2;
        cout <<fixed<<setprecision(1)<<  "Area = "<<A<<endl;
    }
    return 0;
}