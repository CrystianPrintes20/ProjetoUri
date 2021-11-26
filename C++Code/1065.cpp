//Questão: Pares entre Cinco Números
#include <iostream>

using namespace std;

int main()
{
	int n, qtde = 0;
	
	for(int i = 1; i <= 5; i++){
		cin >> n;
	
		if(n%2 == 0){
			qtde += 1;
		}
	}
	cout <<qtde<< " valores pares\n";
	
}