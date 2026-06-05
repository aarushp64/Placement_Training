#include <iostream>
using namespace std;

int main(){
    int x = 10; 
    int* myptr; 
    myptr = &x;
    cout << "Value of x is: ";
    cout << x << endl;
    cout << "Address stored in myptr is: ";
    cout << myptr << endl;
    cout << "Value of x using *myptr is: ";
    cout << *myptr << endl;

     int y = 10;
    int& myref = y;
    y = 30;
    cout << "value of y is " << y << endl;
    cout << "value of myref after change in value of y is: "
         << myref << '\n';

    return 0;
}