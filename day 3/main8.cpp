#include <iostream>
using namespace std;

int main() {
  
  	int num;
    cout << "Enter a number: ";
    cin >> num;
    int temp=num;
    int result=0;

    while(num!=0){
        int d= num%10;
        result+=d*d*d;
        num=num/10;
    }
    if(result==temp){
        cout<<"It is an Armstrong number."<<endl;
    }
    else{
        cout<<"It is not an Armstrong number."<<endl;
    }

    // int n;
    // cout << "Enter a number: ";
    // cin >> n;

    // int square = n * n;
    // int sum = 0;
    // int digit;
        
    // while(square > 0) {
    //     digit = square % 10;
    //     sum += digit;
    //     square /= 10;
    // }
    // if(sum == n) {
    //     cout << n << " is a Neon number." << endl;
    // } else {
    //     cout << n << " is not a Neon number." << endl;
    // }	

    return 0;
}