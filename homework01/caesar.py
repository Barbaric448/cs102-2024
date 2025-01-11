def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'


    for letter in plaintext:
        try:
            if letter in rus_alph:
                ciphertext += rus_alph[(rus_alph.index(letter.lower())+shift)%33]
            else:
                ciphertext += eng_alph[(eng_alph.index(letter.lower())+shift)%26]
        except:
            ciphertext += letter

    ciphertext = list(ciphertext)
    for i, letter in enumerate(plaintext):
        if not letter.islower():
            ciphertext[i] = ciphertext[i].upper()
    ciphertext = ''.join(ciphertext)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'

    for letter in ciphertext:
        try:
            if letter in rus_alph:
                plaintext += rus_alph[(rus_alph.index(letter.lower())-shift)]
            else:
                plaintext += eng_alph[(eng_alph.index(letter.lower())-shift)]
        except:
            plaintext += letter

    plaintext = list(plaintext)
    for i, letter in enumerate(ciphertext):
        if not letter.islower():
            plaintext[i] = plaintext[i].upper()

    plaintext = ''.join(plaintext)    
    return plaintext
