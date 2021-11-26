//Questão: Imposto de renda
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double a,taxa,taxa1,taxa2,total;
    cin >> a;
    
    if (a >= 0 && a <= 2000.00)
    {
       cout << "Isento\n";
    }
    else
    {
        if (a > 2000 && a <= 3000)
        {
            total = ((a - 2000)*8)/100;
        }
        else if (a > 3000 && a <= 4500)
        {
            taxa = a - 3000;
            taxa1 = (1000 *8)/100;
            total = ((taxa * 18)/100) + taxa1;
        }
        else if (a > 4500)
        {
            taxa = (a - 4500);

            taxa1 = (1000 *8)/100;
            taxa2 = (1500 * 18)/100;
            total = ((taxa * 28)/100) +taxa2+taxa1;

        }
        cout<<fixed<<setprecision(2)<< "R$ "<<total<< endl;
    }
    
    
    
    return 0;
}