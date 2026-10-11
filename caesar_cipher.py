def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


print("================================")
print("      CAESAR CIPHER TOOL")
print("================================")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Enter E for Encryption or D for Decryption: ").upper()

if choice == "E":
    encrypted = caesar_cipher(message, shift, "encrypt")
    print("\nEncrypted Message:", encrypted)

elif choice == "D":
    decrypted = caesar_cipher(message, shift, "decrypt")
    print("\nDecrypted Message:", decrypted)

else:
    print("Invalid choice.")
