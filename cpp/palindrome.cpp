#include <iostream>
#include <string>
using namespace std;


int is_palindrome(string palindrome)
{
    int len = palindrome.size();
    int j = len-1;
    for (int i=0; i<(len/2); i++)
    {
        if (palindrome[i] == ' ' && palindrome[j] != ' ')
        {
            continue;
        }
        else if (palindrome[j] == ' ' && palindrome[i] != ' ')
        {
            i--;
            j--;
            continue;
        }
        else if (palindrome[i] != palindrome[j])
        {
            cout << palindrome[j] << ": " << palindrome[i] << endl;
            return 0;
        }
        j--;
    }
    return 1;
}

int main()
{
    string palindrome;

    cout << "Enter a palindrome: ";
    getline (cin, palindrome);

    if (is_palindrome(palindrome))
    {
        cout << palindrome << " is a palindrome!" << endl;
    }
    else 
    {
        cout << palindrome <<  " isn't a palindrome at all!" << endl;
    }

    return 0;
}
