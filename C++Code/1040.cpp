//Questão: Media 3
#include <iostream>
#include <iomanip>
 
 using namespace std;

 int main(){
     double n1,n2,n3,n4, nota_exame, media;
     cin >> n1 >> n2 >> n3 >> n4;
     media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10;

     cout << fixed << setprecision(1)<<"Media: " <<media << endl;

     if (media >= 7.0){
         cout << "Aluno aprovado." << endl;
     }
     else if (media < 5.0)
     {
        cout << "Aluno reprovado." << endl;
     }

     if (media >= 5.0 && media <= 6.9)
     {
        cout << "Aluno em exame." << endl;
        cin >> nota_exame;
        cout << fixed << setprecision(1)<< "Nota do exame: " << nota_exame<< endl;
        media = (media + nota_exame)/2;

        if (media >= 5.0)
        {
            cout << "Aluno aprovado." << endl;
        }
        else
        {
            cout << "Aluno reprovado." << endl;
        }
        cout << fixed << setprecision(1)<< "Media final: " <<media << endl;
        
     }
     return 0;

 }