BLUE = '\033[94m'
RESET = '\033[0m'
art = f"""{BLUE}
                                        _       _               
   ___ __ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __ 
  / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
 | (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
  \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                         |_|                    {RESET}"""
def caesar_cipher(text, shift, encrypt=True):
  
    shifted_text = ""
    for char in text:
        if char.isalpha():
            if encrypt:
                shifted = ord(char) + shift
            else:
                shifted = ord(char) - shift
            
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            
            shifted_text += chr(shifted)
        else:
            shifted_text += char
    
    return shifted_text

def main():
    print(art)
    print("Welcome to the Caesar Cipher program!")
    while True:
        print("\nOptions:" )
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            encrypted_message = caesar_cipher(text, shift)
            print(f"Original message: {text}")
            print(f"Encrypted message: {encrypted_message}")
        
        elif choice == '2':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            decrypted_message = caesar_cipher(text, shift, encrypt=False)
            print(f"Original message: {text}")
            print(f"Decrypted message: {decrypted_message}")
        
        elif choice == '3':
            print("Thank you for using the Caesar Cipher Program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
