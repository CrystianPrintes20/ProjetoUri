//Questão: Numeros Positivos
#include <iostream>
#include <vector>

using namespace std;

int main(){
    float n,qtde;
    vector<float> v;
    for(float i = 0; i < 6; ++i){
        cin >> n;
        v.push_back(n);
        
        if (v[i] > 1)
        {
          qtde += 1;
        }
    }
    cout<<qtde<<" valores positivos\n";
    return 0;
}