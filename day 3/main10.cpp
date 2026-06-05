#include <iostream>
using namespace std;

int main() {
    // Fibonacci series
    int a=0,b=1,c;
    int n;
    cout << "Enter a number: "; 
    cin >> n;
    cout << "Fibonacci series up to " << n << ": ";
    
    for (int i = 0; i < n; i++) {
        cout << a << " ";
        c = a + b;
        a = b;
        b = c;
    }
  	
    return 0;
}