import os

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        text = file.read()
    encrypted_text = caesar_cipher_encrypt(text, shift)
    with open(output_file, 'w') as file:
        file.write(encrypted_text)
    print(f"File '{input_file}' encrypted successfully to '{output_file}'.")

def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        text = file.read()
    decrypted_text = caesar_cipher_decrypt(text, shift)
    with open(output_file, 'w') as file:
        file.write(decrypted_text)
    print(f"File '{input_file}' decrypted successfully to '{output_file}'.")

def main():
    while True:
        print("\nCaesar Cipher File Encryption/Decryption")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            input_file = input("Enter the path of the file to encrypt: ")
            output_file = input("Enter the path of the output encrypted file: ")
            shift = int(input("Enter the shift value for encryption: "))
            if os.path.exists(input_file):
                encrypt_file(input_file, output_file, shift)
            else:
                print("Input file does not exist.")
        elif choice == "2":
            input_file = input("Enter the path of the file to decrypt: ")
            output_file = input("Enter the path of the output decrypted file: ")
            shift = int(input("Enter the shift value for decryption: "))
            if os.path.exists(input_file):
                decrypt_file(input_file, output_file, shift)
            else:
                print("Input file does not exist.")
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
