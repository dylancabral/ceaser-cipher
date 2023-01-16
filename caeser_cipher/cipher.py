import nltk
import re
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names


def encrypt(string, shift):

    ciphertext = ""

    # looping through a string
    for char in string:
        if char.isalpha():
            offset = 97 if char.islower() else 65
            shifted_val = (ord(char) + shift - offset) % 26 + offset
            ciphertext += chr(shifted_val)
        else:
            ciphertext += char
            print("this is the ciphertext: " + ciphertext)

    return ciphertext


def decrypt(ciphertext, shift):
    """
    Reverse encrypt() operation with original key as an argument

    :param ciphertext: string of integers
    :param key: integer
    :return: string of integers
    """
    return encrypt(ciphertext, -shift)


def crack(string):
    for i in range(1, 26):
        attempt = encrypt(string, i)
        word_list = attempt.split()
        count = 0
        for word in word_list:
            word = re.sub(r"[^A-Za-z]+", "", word)
            if word.lower() in words.words() or word in names.words():
                count += 1
        if count / len(word_list) > 0.9:
            return attempt
    return ""


if __name__ == '__main__':
    pass

