//Questão: Tipos de triangulos
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int main()
{
    float x;
    vector<float> v;

    for (int i = 0; i < 3; ++i)
    {
        cin >> x;
        v.push_back(x);
    }

    sort(v.begin(), v.end(), greater<float>());

    if (v[0] >= v[1]+v[2])
    {
        cout << "NAO FORMA TRIANGULO" <<endl;
    }
    else if (pow(v[0],2) == pow(v[1],2) + pow(v[2],2))
    {
         cout << "TRIANGULO RETANGULO"<<endl;
    }
    else if (pow(v[0],2) > pow(v[1],2) + pow(v[2],2))
    {
         cout << "TRIANGULO OBTUSANGULO"<<endl;
    }
    else if (pow(v[0],2) < pow(v[1],2) + pow(v[2],2))
    {
         cout << "TRIANGULO ACUTANGULO"<<endl;
    }
    if ((v[0] == v[1]) && (v[0] == v[2]))
    {
         cout << "TRIANGULO EQUILATERO"<<endl;
    }
    if ( (v[0] == v[1] && v[0] != v[2]) || (v[0] == v[2] && v[0] != v[1]) || (v[1] == v[2] && v[1] != v[0]))
    {
       cout << "TRIANGULO ISOSCELES"<<endl;
    }

    return 0;
}