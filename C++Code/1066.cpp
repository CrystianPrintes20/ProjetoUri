//Questão: Pares, Ímpares, Positivos e Negativos
#include <iostream>

using namespace std;

int main()
{
	int n, par = 0,impar = 0,pos = 0, neg = 0;
	
	for(int i = 1; i <= 5; i++){
		cin >> n;
	
		if(n%2 == 0){
			par += 1;
		}else
        {
            impar += 1;
        }
        if (n > 0)
        {
            pos += 1;
        }else if (n < 0)
        {
           neg += 1;
        }
        
        
	}
	cout <<par<<" valor(es) par(es)\n";
    cout <<impar<<" valor(es) impar(es)\n";
    cout <<pos<<" valor(es) positivo(s)\n";
    cout <<neg<<" valor(es) negativo(s)\n";

    return 0;
	
}