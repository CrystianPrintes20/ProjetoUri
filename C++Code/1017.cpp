//Questão: Gasto de Combustível
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int tempo, velocidade_m ;
    double distancia_p,litrosKm;
    cin >> tempo >> velocidade_m;
    distancia_p = tempo*velocidade_m;
    litrosKm = distancia_p/12;
    cout << fixed << setprecision(3)<<litrosKm << endl;

    return 0;
}