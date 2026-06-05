#include <iostream>
using namespace std;
#include <algorithm>
int main(){
    //program to find duplicate number in the given array
    int arr[10]={10,6,7,32,10,5,7,10,6,7};
    sort(arr, arr + 10);
    for (int i=0;i<9;i++){
        if(arr[i]==arr[i+1]){
            cout << arr[i] << " ";
        }
    }
    return 0;
}