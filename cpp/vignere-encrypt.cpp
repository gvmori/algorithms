#include <iostream>
#include <string>
// #include <cctype>

using namespace std;

void vignere_encrypt(const string &key, string &source)
{
    string out;

    int key_size = key.size();
    for (size_t i=0; i<source.size(); i++)
    {
        source[i] = ((source[i] + key[i%key_size] - 32) % 96 + 32);
    }
}

int main()
{
    string secret_pass_phrase;
    string top_secret_message;

    cout << "enter your SUPER SECRET PASS KEY PHRASE:" << endl << ">> ";
    getline(cin, secret_pass_phrase);

    cout << "now enter your TOP SECRET MESSAGE:" << endl << ">> ";
    getline(cin, top_secret_message);

    vignere_encrypt(secret_pass_phrase, top_secret_message);

    cout << top_secret_message << endl;
    return 0;
}
