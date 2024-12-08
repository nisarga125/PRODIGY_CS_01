def caesar_cipher(text, shift, mode):
    """
    Encrypt or decrypt text using the Caesar Cipher algorithm.

    :param text: str - The input text to encrypt or decrypt.
    :param shift: int - The shift value for the Caesar Cipher.
    :param mode: str - "encrypt" or "decrypt".
    :return: str - The encrypted or decrypted text.
    """
    result = ""
    if mode == "decrypt":
        shift = -shift  

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
           
            result += char
    return result

def main():
    print("Caesar Cipher Encryption and Decryption")
    mode = input("Would you like to 'encrypt' or 'decrypt' a message? ").strip().lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid option. Please enter 'encrypt' or 'decrypt'.")
        return

    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid input. Shift value must be an integer.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"\nThe {mode}ed message is: {result}")

if __name__ == "__main__":
    main()
