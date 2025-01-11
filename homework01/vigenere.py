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

    keyword = keyword * (len(plaintext) // len(keyword)) + keyword[: len(plaintext) % len(keyword)].lower()

    for i in range(len(plaintext)):
        try:
            if plaintext[i] in rus_alph:
                ciphertext += rus_alph[(rus_alph.index(plaintext[i].lower()) + rus_alph.index(keyword[i].lower())) % 33]
            else:
                ciphertext += eng_alph[(eng_alph.index(plaintext[i].lower()) + eng_alph.index(keyword[i].lower())) % 26]
        except:
            ciphertext += plaintext[i]

    newCiphertext = list(ciphertext)

    for i, letter in enumerate(plaintext):
        if not letter.islower():
            newCiphertext[i] = newCiphertext[i].upper()
    ciphertext = "".join(newCiphertext)

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

    keyword = keyword * (len(ciphertext) // len(keyword)) + keyword[: len(ciphertext) % len(keyword)].lower()

    for i in range(len(ciphertext)):
        try:
            if ciphertext[i] in rus_alph:
                plaintext += rus_alph[(rus_alph.index(ciphertext[i].lower()) - rus_alph.index(keyword[i].lower()))]
            else:
                plaintext += eng_alph[(eng_alph.index(ciphertext[i].lower()) - eng_alph.index(keyword[i].lower()))]
        except:
            plaintext += ciphertext[i]

    newPlaintext = list(plaintext)

    for i, letter in enumerate(ciphertext):
        if not letter.islower():
            newPlaintext[i] = newPlaintext[i].upper()
    plaintext = "".join(newPlaintext)

    return plaintext
