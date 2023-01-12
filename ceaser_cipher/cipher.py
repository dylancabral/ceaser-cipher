import nltk
import ssl
import re

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

    nltk.download("words", quiet= true )
    nltk.download("names", quiet= true)

def count_words(text):
    # string.split() list of words in string by given character split
    # "hi hello" -> ["hi", "hello"]
    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        candidate = re.sub(r"[^A-Za-z]+", "", candidate)
        if candidate.lower() in word_list or candidate in name_list:
            word_count += 1

    return word_count


def encrpyt():
  """
  Takes in a string integers representing the plaintext, and return a new string of integers
  shifted by a key, mod 10 ("number wrap")
  :param plaintext: string of integers
  :param key: integer
  :return: string of integers
  """
  ciphertext = ""

  # looping through a string
  for char in plaintext:
      # "3" -> 3
      num = int(char)
      shift_num = (num + key) % 10  # e.g. 12 % 10 -> 2
      # build up the ciphertext string
      ciphertext += str(shift_num)

  return ciphertext



def decrypt(string , shift):
    return encrpyt(string, shift*(-1))



def crack():
  pass


