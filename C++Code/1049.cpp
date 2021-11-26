//Questão: Animal
#include <iostream>
#include <cstring>

using namespace std;

int main(){
    string animal;
    cin>> animal;

    if (animal == "vertebrado")
    {
       cin >> animal;
       if (animal == "ave")
       {
           cin >> animal;
           if (animal == "carnivoro")
           {
               cout << "aguia\n";
           }
           if (animal == "onivoro")
           {
               cout << "pomba\n";
           }
       }
       if (animal == "mamifero")
       {
           cin >> animal;
           if (animal == "onivoro")
           {
               cout << "homem\n";
           }
           if (animal == "herbivoro")
           {
               cout << "vaca\n";
           }
       }
    }

     if (animal == "invertebrado")
    {
       cin >> animal;
       if (animal == "inseto")
       {
           cin >> animal;
           if (animal == "hematofago")
           {
               cout << "pulga\n";
           }
           if (animal == "herbivoro")
           {
               cout << "lagarta\n";
           }
       }
       if (animal == "anelideo")
       {
           cin >> animal;
           if (animal == "hematofago")
           {
               cout << "sanguessuga\n";
           }
           if (animal == "onivoro")
           {
               cout << "minhoca\n";
           }
       }
    }

    return 0;
    
}