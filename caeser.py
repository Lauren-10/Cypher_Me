'''
shift cipher
'''

def decrypt_caesar(ciphertext, key):
    """Decrypts a Caesar cipher.

    Args:
        ciphertext: The text to decrypt.
        key: The shift value used for encryption.

    Returns:
        The decrypted text.
    """
    decrypted_text = ""
    #shift over each character one by one
    for char in ciphertext:
        #we enter this conditional if the character if a letter (A-Z)
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start - key) % 26 + start)
        elif char.isdigit():
             shifted_char = str((int(char) - key) % 10)
        else:
            shifted_char = char
        decrypted_text += shifted_char
    return decrypted_text

if __name__ == "__main__":
    ciphertext = "huapkval"
    decoded_string = ""
    for i in range(1,26):
        decoded_string = decrypt_caesar(ciphertext, i)
        print(f"Key {i}: {decoded_string}")
    