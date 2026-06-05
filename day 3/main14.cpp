#include <iostream>
#include <conio.h>
int nSum(int n);
void main() {
    int n=15;
    int sum = nSum(n);
    printf("Sum of first %d natural numbers is: %d", n, sum);
    getch();
}

int nSum(int n)
{
    if (n == 0) {
        return 0;
    }
    int res = n + nSum(n - 1);
    return res;
}
