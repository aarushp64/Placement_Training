#include <iostream>
using namespace std;

int main() {
  

    // for (int i = 1; i <= 10; i++) {
    //     cout << i << " ";
    

    int n,c;
    cout << "Enter a number: ";
    cin >> n;
    // cout<< "Natural numbers from 1 to " << n << " are: ";
    // for (int i = 1; i <= n; i++) {
    //     cout << i << " ";
    // }
    
    // cout << "Even numbers from 1 to " << n << " are: ";
    // for (int i = 1; i <= n; i++) {
    //     if (i % 2 == 0) {
    //         cout << i << " ";
    //     }
    // }
    // cout << endl;
    // cout << "Odd numbers from 1 to " << n << " are: ";
    // for (int i = 1; i <= n; i++) {
    //     if (i % 2 != 0) {
    //         cout << i << " ";
    //     }
    // }
    
    for (int i=2;i<=n;i++){
        if(n%i==0){
            cout << "Not a prime number.";
            c++;
            break;
        }
    }
    if(c==0){
        cout << "Prime number.";
    }

    return 0;
}