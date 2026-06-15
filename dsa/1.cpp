#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}
int subtract(int a, int b) {
    return a - b;
}
int multiply(int a, int b) {
    return a * b;
}
int divide(int a, int b) {
    return a / b;
}
int mod(int a, int b) {
    return a % b;
}

int main() {
    int a, b;
    char opr;
    char choice;
    cout<<"Enter two numbers: ";
    cin>>a>>b;
    do {
        cout << "Enter operator (+,-,*,/,%): ";
        cin >> opr;
        switch(opr) {
            case'+':
                cout<<"Addition: " <<add(a, b)<<endl;
                break;
            case'-':
                cout<<"Subtraction: "<<subtract(a, b)<<endl;
                break;
            case'*':
                cout<<"Multiplication: "<<multiply(a, b)<<endl;
                break;
            case '/':
                cout << "Division: " <<divide(a, b)<<endl;
                break;
            case '%':
                cout<<"Modulus: " <<mod(a, b)<<endl;
                break;
            default:
                cout<< "Invalid operator"<<endl;
        }
        cout << "Do you want to continue? (y/n): ";
        cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    return 0;
}