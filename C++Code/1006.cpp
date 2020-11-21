//Questão: Media 2
#include <iostream>
#include <iomanip>
using namespace std;
int main(int argc, char const *argv[]) {
  float a,b,c,total;
  cin >> a >> b >> c;
  cout << fixed <<setprecision(1);
  cout << "MEDIA = "<< ((2 * a)+(3 * b)+(c * 5))/10 << endl;
  return 0;
}