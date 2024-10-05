The encryption algorithm implemented in this program uses a variable shift substitution cipher that alters the character of a given text based on a key provided by the user. The encryption and decryption functions work by manipulating the Unicode values of the characters in the text, and the program is designed to handle input and output through text files.

# Encryption Algorithm:
The encryption algorithm takes in two inputs:
**Text file:** The string of characters to be encrypted or decrypted in a .txt file.
**Key:** An integer between 1 and 100 that defines the amount by which each character's Unicode value will be shifted.

For each character in the input text:
The algorithm calculates the shift value for that character. The shift is based on the formula:
Shift=Key + Index + Key^2
where the Key is a user-provided integer, and Index is the position of the character in the text (starting from 0).
The Unicode value of the character is retrieved using the ord() function, and the calculated shift value is added to it to determine the new Unicode value. The new character is generated using the chr() function.

# Encryption Process:
Each character in the text is shifted forward by a variable amount determined by the formula above. This process continues until all characters are shifted and concatenated into the encrypted result.
Decryption Process:
Decryption works similarly to encryption but in reverse. The same shift value is calculated for each character in the encrypted text, but instead of adding the shift value, it is subtracted from the Unicode value to revert to the original character.

# Program Flow:
The program can either encrypt or decrypt a file using the above algorithm. The user can input a file name containing the text to be encrypted/decrypted, the output file name to save the result, and a key.
Program Structure:
**1. encrypt_shift():**
This function encrypts a given string based on the key and index position of each character.

**2. decrypt_shift():**
This function reverses the encryption by shifting the characters back to their original values.

**3. encrypt_file():**
This function reads the content of a file, encrypts each line using encrypt_shift(), and writes the encrypted lines to a new file.

**4. decrypt_file():**
This function performs the opposite of encrypt_file(), decrypting each line of the input file and saving the decrypted content to an output file.

**5. User Interaction:**
The program prompts the user to choose between encryption or decryption and to provide the necessary input and output file names along with the key.

