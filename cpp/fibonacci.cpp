#include <iostream>
using namespace std;

int fibonacci(int f)
{
    int j = 1;
    int k = 0;
    for (int i; i<f; i++)
    {
        int h = k;
        k += j;
        j = h;
    }
    return k;
}

int main()
{
    int f;
    cout << "Enter an integer: ";
    cin >> f;
    int k = fibonacci(f);
    cout << "the " << f << "th fibonacci number is: " << k << endl;

    return 0;
}
