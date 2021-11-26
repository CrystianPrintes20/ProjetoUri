//Questão: Seis Números Ímpares
#include <iostream>

using namespace std;

int main()
{
	int i, n;
	cin >> n;
	
	
    if (n%2 == 0)
    {
        n += 1;
        for(i = n; i <= n+10; i += 2){
              cout << i << endl;
        }
      
    }else 
    {
        cout<< "hdds"<< endl;
        for(i = n; i <= n+10; i += 2){
              cout << i << endl;
        }
    }
    return 0;
	
}