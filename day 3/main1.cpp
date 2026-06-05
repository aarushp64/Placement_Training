#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!" << endl;
    int a,b;
    cout << "Enter two integers: ";
    cin >> a >> b;

    cout << "a = " << a << ", b = " << b << endl;
    // Addition, Subtraction, Multiplication, Division, Modulo
    cout << "a + b = " << (a + b) << endl;
    cout << "a - b = " << (a - b) << endl;
    cout << "a * b = " << (a * b) << endl;
    cout << "a / b = " << (a / b) << endl;
    cout << "a % b = " << (a % b) << endl;
    // Increment, Decrement
    cout << "++a = " << ++a << endl;
    cout << "b-- = " << b-- << endl;
    // Comparison operators
    cout << "a == b is " << (a == b) << endl;//Equal to operator
    cout << "a > b is " << (a > b) << endl;//Greater than operator
    cout << "a >= b is " << (a >= b) << endl;//Greater than or equal to operator
    cout << "a < b is " << (a < b) << endl;//Less than operator
    cout << "a <= b is " << (a <= b) << endl;//Less than or equal to operator
    cout << "a != b is " << (a != b) << endl;//Not equal to operator
    // Logical operators
    cout << "a && b is " << (a && b) << endl;//And operator
    cout << "a || b is " << (a || b) << endl;//Or operator
    cout << "!b is " << (!b) << endl;//Not operator
    return 0;
}
