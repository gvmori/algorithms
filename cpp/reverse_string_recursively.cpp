#include <iostream>
#include <string>
using namespace std;

void reverse (string &string_to_reverse, int i, int length)
{
    if (i > length/2)
    {
        return;
    }
    char placeholder = string_to_reverse[i];
    string_to_reverse[i] = string_to_reverse[length-1-i];
    string_to_reverse[length-1-i] = placeholder;
    i++;
    reverse(string_to_reverse, i, length);
}

int main()
{
    string string_to_reverse;

    cout << "enter a line to be reversed:" << endl << ">> ";
    getline(cin, string_to_reverse);
    reverse(string_to_reverse, 0, string_to_reverse.size());

    cout << string_to_reverse << endl;
}
