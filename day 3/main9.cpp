#include <iostream>
using namespace std;

int main() {
    int a;
    cout << "Enter a number: ";
    cin >> a;
    int fact=1;
    for(int i=1;i<=a;i++){  
        fact=fact*i;  
    }
    cout<<"Factorial of "<<a<<" is: "<<fact<<endl;

    //strong number
    int temp=a;
    int result=0;   
    while(temp!=0){
        int d= temp%10;
        int f=1;
        for(int i=1;i<=d;i++){
            f=f*i;
        }
        result+=f;
        temp=temp/10;
    }
    if(result==a){
        cout<<"It is a Strong number."<<endl;
    }
    else{
        cout<<"It is not a Strong number."<<endl;
    }

    return 0;
}