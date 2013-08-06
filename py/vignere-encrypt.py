#!/usr/bin/python

def vignere_encrypt(key_phrase, message):
    out_message = []
    for i in xrange(len(message)):
        out_message.append(chr((ord(message[i]) + ord(key_phrase[i%len(key_phrase)]) - 32) % 96 + 32))

    return "".join(out_message)

def main():
    print "enter your secret key phrase:\n>>",
    key_phrase = raw_input()

    print "now enter your top secret message:\n>>",
    message = raw_input()

    message = vignere_encrypt(key_phrase, message)

    print message

if __name__ == '__main__':
    main()