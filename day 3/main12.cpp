#include <iostream>
using namespace std;
int main(){
    int n;
    cout << "Enter a number: ";
    cin >> n;

    while(n>1){
        if (n%2!=0){
            cout << "Not a Power of 2.";
            return 0;
        }
        n/=2;
    }
    cout << "Is a Power of 2.";
    return 0;
}