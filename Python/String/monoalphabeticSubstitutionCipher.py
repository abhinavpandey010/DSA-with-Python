def monoalphabetic_encrypt(plaintext, mapping):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()
    ciphertext = ""

    for ch in plaintext:
        if ch in alphabet:
            idx = alphabet.index(ch)
            ciphertext += mapping[idx]
        else:
            ciphertext += ch
    return ciphertext


def monoalphabetic_decrypt(ciphertext, mapping):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()
    plaintext = ""

    for ch in ciphertext:
        if ch in mapping:
            index = mapping.index(ch)
            plaintext += alphabet[index]
        else:
            plaintext += ch
    return plaintext


mapping = "QWERTYUIOPASDFGHJKLZXCVBNM"
pt = input("Enter Plain text : ")
ct = monoalphabetic_encrypt(pt, mapping)
print("Encrypted:", ct)
print("Decrypted:", monoalphabetic_decrypt(ct, mapping))
