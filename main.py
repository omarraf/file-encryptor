def encrypt_shift(text, key):
    encrypted_text = []
    for i, char in enumerate(text): 
        new_char = chr(ord(char) + (key + i + key ** 2))
        encrypted_text.append(new_char)
    return ''.join(encrypted_text)
    

def decrypt_shift(text, key):
    decrypted_text = []
    for i, char in enumerate(text):
        new_char = chr(ord(char) - (key + i + key ** 2))
        decrypted_text.append(new_char)
    return ''.join(decrypted_text)    


def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        with open(output_file, 'w') as file:
            for line in lines:
                file.write(encrypt_shift(line, key))
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")

def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        with open(output_file, 'w') as file:
            for line in lines:
                file.write(decrypt_shift(line, key))

    except FileNotFoundError:
        print(f"Error: {input_file} not found!")

if __name__ == "__main__":
    print("Press 'e' to Encrypt a file")
    print("Press 'd' to Decrypt a file")
    
    choice = input("Enter your choice: ")
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    while True:
        try:
            key = int(input("Enter the encryption/decryption key (integer): 1 - 100: "))
            if 1 <= key <= 100: 
                break  
            else:
                print("Key must be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if choice == "e":
        encrypt_file(input_file, output_file, key)
    elif choice == "d":
        decrypt_file(input_file, output_file, key)
    else:
        print("Invalid choice, please select 'e' or 'd'.")
    