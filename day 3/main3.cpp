#include <iostream>
using namespace std;
int main(){
    char status;
    cout << "Enter your Promotion status (P for Promoted, W for Working on site and B for Bonus): ";
    cin >> status;
    if (status == 'P') {
        cout << "You are not eligible for WFH.";
    }
    else if (status == 'W'&& status == 'B') {
        cout << "You are not eligible for WFH.";
    }
    else if (status == 'B' && status != 'W') {
        cout << "You are eligible for WFH.";
    }
    else {
        cout << "Invalid input. Please enter P, W, or B.";
    }
    return 0;
}