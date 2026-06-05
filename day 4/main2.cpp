#include <iostream>
using namespace std;

int main() {
    // int arr[] = {10,20,30,40,50};
    // for (int i = 0; i < 5; i++)
    // cout << arr[i] << " ";
    // cout << arr[1] << " ";
    // cout << arr[4];

    // int arr[10] = {8, 7, 11, 12, 42, 23, 17, 38, 18, 22};
    // int even = 0;
    // int odd = 0;
    // cout << "Even numbers in the array: ";
    // for (int i = 0; i < 10; i++) {
    //     if (arr[i] % 2 == 0) {
    //         cout << arr[i] << " ";
    //         even++;    
    //     }
    // }
    // cout << endl;
    // cout << "Number of even numbers: " << even << endl;
    // cout << "Odd numbers in the array: ";
    // for (int i = 0; i < 10; i++) {
    //     if (arr[i] % 2 != 0) {
    //         cout << arr[i] << " ";
    //         odd++;
    //     }
    // }
    // cout << endl;
    // cout << "Number of odd numbers: " << odd << endl; 

    int max=0, max2=0;
    int arr[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    for (int i = 0; i < 10; i++) {
        if (arr[i] > max) {
            max2 = max;
            max = arr[i];
        } else if (arr[i] > max2) {
            max2 = arr[i];
        }
    }
    cout << "Maximum number: " << max << endl;
    cout << "Second maximum number: " << max2 << endl;
    
    return 0;
}