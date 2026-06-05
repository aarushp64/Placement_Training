#include <iostream>
using namespace std;
#include <algorithm>

int main(){
    int arr[10]= {1,2,3,4,5,6,7,8,9,10};
    int target = 14;
    int a=0, b=9;
    while (a < b){
        if(arr[a] + arr[b] == target){
            cout<< "Pair found: " << arr[a] << " " << arr[b] << endl;
            break;
        }else if (arr[a] + arr[b] < target){
            a+=1;
        }else{
            b-=1;
        }
    }
    if (a >= b) {
        cout << "No such pair found." << endl;
    }
    return 0;
}