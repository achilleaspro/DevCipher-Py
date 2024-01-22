#function to calculate the multiplicative inverse of a number
def multiplicative_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i
    return -1

#function to calculate greatest common divisor of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#function to encrypt a plaintext message
def encrypt(plaintext, a, b):
    ciphertext = ""
    for letter in plaintext:
        #convert letter to uppercase
        letter = letter.upper()
        #check if letter is in the alphabet
        if letter.isalpha():
            #get the ASCII value of the letter
            char_value = ord(letter)
            #subtract 65 from the ASCII value in the range 0-25
            char_value -= 65
            #encrypt the letter using Affine Cipher formula
            entrypted_value = (a * char_value + b) % 26
            #add 65 to get the ASCII value of the encrypted letter
            entrypted_value += 65
            #add encrypted letter to the ciphertext
            ciphertext += chr(entrypted_value)

    return ciphertext

#function to decrypt a ciphertext message
def decrypt(ciphertext, a, b):
    plaintext = ""
    a_inverse = multiplicative_inverse(a)
    for letter in ciphertext:
        #convert letter to uppercase
        letter = letter.upper()
        #check if letter is in the alphabet
        if letter.isalpha():
            #get the ASCII value of the letter
            char_value = ord(letter)
            #subtract 65 from the ASCII value in the range 0-25
            char_value -= 65
            #decrypt the letter using Affine Cipher formula
            decrypted_value = (a_inverse * (char_value - b)) % 26
            #add 65 to get the ASCII value of the decrypted letter
            decrypted_value += 65
            #add decrypted letter to the plaintext
            plaintext += chr(decrypted_value)

    return plaintext

#main function
def main():
    while True:

        #read the mode from the user
        mode = int(input("\nEnter 1 to encrypt or 2 to decrypt: "))

        if mode == 1:
            a= int(input("Enter the value of A: "))
            b = int(input("Enter the value of B: "))

            #check the validity of keys
            if gcd(a, 26) != 1:
                print("Invalid keys. 'A' must be co-prime with 26.")
                return
            if b > 25 or b<0:
                print("Invalid keys. 'B' must be less than 26 and more than -1.")
                return
            
            #read the plaintext from the user
            plaintext = input("Enter the plaintext: ")
            print("The ciphertext is: ", encrypt(plaintext, a, b))
            return

        elif mode == 2:
            a = int(input("Enter the value of A: "))
            b = int(input("Enter the value of B: "))

            #check the validity of keys
            if gcd(a, 26) != 1:
                print("Invalid keys. 'A' must be co-prime with 26.")
                return
            if b > 25 or b<0:
                print("Invalid keys. 'B' must be less than 26 and more than -1.")
                return


            #read the ciphertext from the user
            ciphertext = input("Enter the ciphertext: ")
            print("The plaintext is:", decrypt(ciphertext, a, b))

            #print the multiplicative inverse of a
            print("Multiplicative inverse of A is:", multiplicative_inverse(a))
            return

        else:
            print("Invalid mode. Enter 1 or 2.")
              

if __name__ == "__main__":
    main()
        