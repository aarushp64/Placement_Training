#include <iostream>
using namespace std;
int main()
{
    int a;
    cout << "Enter your age: ";
    cin >> a;
    if (a > 18) {
        cout << "You are over 18, You can vote.";
    }
    else if (a == 18) {
        cout << "You are 18, You can vote but you have to make Voter ID first.";
    }
    else {
        cout << "You are not over 18, You can't vote yet.";
    }

    return 0;
}