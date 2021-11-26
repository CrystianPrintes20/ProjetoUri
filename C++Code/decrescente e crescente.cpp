//Questão: Tipos de triangulos
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int a;
    vector<int> v;

    for (int i = 0; i < 3; ++i){
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end()); //, greater<int>() serve para deixar em ordem decrescente
    for(auto x:v){
        cout << x << " ";
    }
    return 0;
}