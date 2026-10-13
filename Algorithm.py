
vowels = "aeiouAEIOU"

def username(first, last):
    return last.lower() + "_" + first[0].lower()


def noVowels(text):
    return "".join(char for char in text if char not in vowels)


def encode_word(word: str) -> str:
    char_list = list(word.strip())
    reordered = []

    for i in range(0, len(char_list), 2):
        reordered.append(char_list[i])

    for i in range(1, len(char_list), 2):
        reordered.append(char_list[i])

    return "".join(reordered)


def decode(word):
    middle = (len(word) + 1) // 2
    first = word[:middle]
    second = word[middle:]

    original = ""
    for i in range(len(second)):
        original += first[i] + second[i]

    if len(first) > len(second):
        original += first[-1]

    return original