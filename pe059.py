"""
XOR decryption
Problem 59

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a
file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum of
the ASCII values in the original text.
"""


def englishChar(i):
    """
    Determines if the integer i corresponds to a valid English character.
    """
    return (chr(i) in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
                      "?!'\"();:0123456789")


def answer():
    with open('cipher.txt') as f:
        # cipher.txt is only 1 line
        # Make a list of ints
        for line in f:
            cipher = map(int, line.strip().split(','))

        deciphered = [None]*len(cipher)

        for pos in xrange(3):
            for a in xrange(97, 123):
                for i in xrange(pos, len(cipher), 3):
                    # English chars are ASCII 32 through 126
                    char = a ^ cipher[i]
                    if not englishChar(char):
                        # Not valid, break and try next letter for key
                        break
                    else:
                        # Is still valid, move into deciphered
                        deciphered[i] = char

                else:
                    # All letters were valid, move on to next letter in key
                    break
            else:
                return "Uh Oh"
    return sum(deciphered)


if __name__ == "__main__":
    print answer()