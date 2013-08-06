#include <iostream>
#include <string>
// #include <cctype>

using namespace std;

void vignere_decrypt(const string &key, string &source)
{
    for (size_t i=0; i<source.size(); i++)
    {
        source[i] = ((source[i] - key[i%key.size()] - 32) % 96 + 128);
        if (source[i] == char(128))
        {
            source[i] = char(32);
        }
    }
}

int main()
{
    string secret_pass_phrase;
    string top_secret_message;

    cout << "enter your EXTRA SECRET DECODER KEY:" << endl << ">> ";
    getline(cin, secret_pass_phrase);

    cout << "now enter your encrypted TOP SECRET MESSAGE:" << endl << ">> ";
    getline(cin, top_secret_message);

    vignere_decrypt(secret_pass_phrase, top_secret_message);

    cout << top_secret_message << endl;
    return 0;
}
