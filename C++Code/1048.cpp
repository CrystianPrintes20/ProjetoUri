//Questão: Aumento de Sálario
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double salario,novosalario, reajuste, perc;
    cin >> salario;

    if (salario >= 0 && salario <= 400)
    {
       reajuste= (salario*15/100);
       novosalario = reajuste + salario;
       perc = 15;
    }
    else if (salario > 400 && salario <= 800)
    {
        reajuste= (salario*12/100);
        novosalario = reajuste + salario;
        perc = 12;
    }
    else if (salario > 800 && salario <= 1200)
    {
        reajuste= (salario*10/100);
        novosalario = reajuste + salario;
        perc = 10;
    }
    else if (salario > 1200 && salario <= 2000)
    {
        reajuste= (salario*7/100);
        novosalario = reajuste + salario;
        perc = 7;
    }
    else if (salario > 2000)
    {
        reajuste= (salario*4/100);
        novosalario = reajuste + salario;
        perc = 4;
    }
    
    cout <<fixed<<setprecision(2)<< "Novo salario: "<<novosalario<<endl;
    cout <<fixed <<setprecision(2)<< "Reajuste ganho: "<<reajuste<<endl;
    cout <<fixed<<setprecision(0)<<"Em percentual: "<<perc<<" %"<<endl;
}