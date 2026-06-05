#include <iostream>
using namespace std;
#include <algorithm>
int main() {
    //making greatest number out of digits in array e.g. 5,2,5,8,8,0 will give 885520
    
    // int res = 0;
    // int arr[]={5,2,5,8,8,0};
    // for(int i=0;i<6;i++){
    //     for(int j=i+1;j<6;j++){
    //         if(arr[i]<arr[j]){
    //             int temp=arr[i];
    //             arr[i]=arr[j];
    //             arr[j]=temp;
    //         }
    //     }
    // }
    // for(int i=0;i<6;i++){
    //     res = res * 10 + arr[i];
    // }
    // cout << res << endl;
    
    int arr[9]= {1,2,3,4,5,6,7,8,9};
    int res = 0 ;
    sort(arr, arr + 9, greater<int>()) ;
    for (int i = 0 ; i < 9 ; i++) {
    res = res * 10 + arr[i] ;
    }
    cout << res ;
    

    // int arr[6] = {1,2,3,8,9,9};
    // int res[10]={0};
    // for (int i=0;i<6;i++){
    //     res[arr[i]]++;
    // }
    // int out=0;
    // for (int i=9;i>=0;i--){
    //     for (int j=0;j<res[i];j++){
    //         out = out * 10 + i;
    //     }
    // }
    // cout << out << endl;

    return 0;
}