#include <iostream>
using namespace std;    

int main() {
    int a, b;
    cout << "Enter two integers: ";
    cin >> a >> b;
    cout << "Before swapping: a = " << a << ", b = " << b << endl;
    swap(a, b);
    cout << "After swapping: a = " << a << ", b = " << b << endl;
    
    return 0;
}


void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
   
}
