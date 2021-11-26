//Questão: Mês
#include <iostream>
#include <cstring>

using namespace std;

int main(){
    int x;
    cin >> x;
    string meses[12] = {"January","February","March","April","May","June","July","August","September","October","November","December"};
    cout << meses[x-1] << endl;

    return 0;
}