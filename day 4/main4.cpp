#include <iostream>
using namespace std;
#include <algorithm>
int main(){
    //program to find the missing number in the given array
    // int arr[6] = {7,5,3,4,1,6};
    // int temp[10]={0};
    // for (int i=0;i<6;i++){
    //     temp[arr[i]]++;
    // }
    // int missing = 0;
    // for (int i=1;i<=7;i++){
    //     if (temp[i] == 0){
    //         missing = i;
    //     }
    // }

    int arr[6] = {7,5,3,4,1,6};
    sort(arr, arr + 6);
    int missing = 0;
    for (int i = 0; i < 6; i++) {
        if (arr[i] != i + 1) {
            missing = i + 1;
            break;
        }
    }
    cout << "Missing number: " << missing << endl;

    return 0;
}