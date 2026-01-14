def xor_encrypt_decrypt(text, key):
    result = ""
    for ch in text:
        result += chr(ord(ch) ^ key)
    return result

plaintext = input("Enter Plain text : ")
key = 12

cipher = xor_encrypt_decrypt(plaintext, key)
print("Encrypted:", cipher)

decrypted = xor_encrypt_decrypt(cipher, key)
print("Decrypted:", decrypted)
