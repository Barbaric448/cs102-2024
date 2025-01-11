def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    eng_alph = "abcdefghijklmnopqrstuvwxyz"

    def expand(word, key):
        if len(word) < len(key):
            return key[: len(word)]

        full = len(word) // len(key)
        tail = len(word) % len(key)

        output = key * full
        output += key[:tail]

        return output

    keyword = expand(plaintext, keyword).lower()

    for i in range(len(plaintext)):
        try:
            if plaintext[i] in rus_alph:
                ciphertext += rus_alph[(rus_alph.index(plaintext[i].lower()) + rus_alph.index(keyword[i].lower())) % 33]
            else:
                ciphertext += eng_alph[(eng_alph.index(plaintext[i].lower()) + eng_alph.index(keyword[i].lower())) % 26]
        except:
            ciphertext += plaintext[i]

    ciphertext = list(ciphertext)
    for i, letter in enumerate(plaintext):
        if not letter.islower():
            ciphertext[i] = ciphertext[i].upper()
    ciphertext = "".join(ciphertext)

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    eng_alph = "abcdefghijklmnopqrstuvwxyz"

    def expand(word, key):
        if len(word) < len(key):
            return key[: len(word)]

        full = len(word) // len(key)
        tail = len(word) % len(key)

        output = key * full
        output += key[:tail]

        return output

    keyword = expand(ciphertext, keyword).lower()

    for i in range(len(ciphertext)):
        try:
            if ciphertext[i] in rus_alph:
                plaintext += rus_alph[(rus_alph.index(ciphertext[i].lower()) - rus_alph.index(keyword[i].lower()))]
            else:
                plaintext += eng_alph[(eng_alph.index(ciphertext[i].lower()) - eng_alph.index(keyword[i].lower()))]
        except:
            plaintext += ciphertext[i]

    plaintext = list(plaintext)
    for i, letter in enumerate(ciphertext):
        if not letter.islower():
            plaintext[i] = plaintext[i].upper()
    plaintext = "".join(plaintext)

    return plaintext
