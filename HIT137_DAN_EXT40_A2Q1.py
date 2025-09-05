"""
Hit137: Team Dan_Ext40

Assignment 2: Question 1

Program: HIT137_DAN_EXT40_A2Q1.py

Authors: Maharun Momo Islam, Moneya Islam, Andrew Morris, Kudzaishe Mutyasira

Last date modified: 05/09/25

Encryption / Decryption:

The purpose of this program is to encrypt a text file by accepting two shift 
numbers from the user and use them to create four keys that will shift the 
characters up or down depending on their case and position in the alphabet.
In the process it will create a fifth key to allow decryption. As there is 
no wrap around of characters, this allows shifting well beyond the alphabet, 
making simple shift reversal during decryption difficult without the fifth 
key, adding an extra layer of security. It will then save the encrypted text
file, load that file, decrypt it with the five keys, and save it again. It
will then load the original text file and verify that it matches the
decrypted file.

"""

# Accept shift numbers from user
shift1 = int (input("Please enter first shift number: "))
shift2 = int (input("Please enter second shift number: "))

# Create encryption keys    
key1 = shift1 * shift2
key2 = - shift1 + - shift2
key3 = - shift1
key4 = shift2 ** 2


def main():

    """The main function of this program"""
       
    encrypt()  # Encrypt raw_text.txt file
            
    print("File encrypted!")
    print("Encrypted text file saved.")
        
    
    decrypt()  # Decrypt encrypted_text.txt file

    print("File decrypted!")
    print("Decrypted text file saved.")

    
    verify()  # Compare decrypted_text to original raw_text file
   

def encrypt():

    """Function to encrypt the raw_txt.txt file and save as encrypted_text.txt"""

    file_raw = open("raw_text.txt", "r")
    raw_text = file_raw.read()

    encrypted_text = ""
    key5 = ""

    
    for ch in raw_text:  # setup a loop to process one character at a time from loaded raw_text file
       
        if ch >= chr(97) and ch <= chr(109):  # First half of lower case alphabet rule, (a - m)
            echr = ord(ch) + key1  # Shift character with key1
            encrypted_text = encrypted_text + chr(echr) # Add shifted character to variable
            key5 = key5 + "1" # Add key number to key sequence

        elif ch >= chr(110) and ch <= chr(122):  # Second half of lower case alphabet rule, (n - z)
            echr = ord(ch) + key2   # Shift character with key2
            encrypted_text = encrypted_text + chr(echr)  # Add shifted character to variable
            key5 = key5 + "2"   # Add key number to key sequence

        elif ch >= chr(65) and ch <= chr(77):  # First half of upper case alphabet rule, (A - M)
            echr = ord(ch) + key3   # Shift character with key3
            encrypted_text = encrypted_text + chr(echr)   # Add shifted character to variable
            key5 = key5 + "3"  # Add key number to key sequence

        elif ch >= chr(78) and ch <= chr(90):  # Second half of upper case alphabet rule, (N -Z)
            echr = ord(ch) + key4   # Shift character with key4
            encrypted_text = encrypted_text + chr(echr)   # Add shifted character to variable
            key5 = key5 + "4"  # Add key number to key sequence
        else:
            encrypted_text = encrypted_text + ch  # Spaces, tabs, newlines, special characters, and numbers remain unchanged
            key5 = key5 + "0"  # Add key number to key sequence (0 = no key)

    # Test mode
    #print (key1, key2, key3, key4)
    #print(raw_text)  
    #print(encrypted_text) 
    #print(key5)  

    # Save encrypted_text file    
    file_e = open("encrypted_text.txt", "w", encoding = "utf-8")  # encoding allows extended character range
    file_e.write(str(encrypted_text))
    file_e.close

    # Save key_text file
    file_k = open("key5.txt", "w")
    file_k.write(str(key5))
    file_k.close     


def decrypt():

    """Function to decrypt the encrypted_text file"""

    file_e = open("encrypted_text.txt", "r", encoding = "utf-8")  # encoding allows extended character range
    etext = file_e.read()

    file_k = open("key5.txt", "r")
    ktext = file_k.read()

    print("Encrypted text file loaded")

    decrypted_text = ""
    key_sequence = 0

    
    for echr in etext:  # setup a loop to process one character at a time from loaded encrypted_text file

        key5 = ktext[key_sequence]  # Step through key5 elements

        if key5 == "1":  # Select appropriate key for decryption 
            dchr = ord(echr) - key1  # Reverse decryption with key1
            decrypted_text = decrypted_text +chr(dchr)  # Add decrypted character to variable
            key_sequence = key_sequence + 1  # Progress forward through key5 sequence

        elif key5 == "2":  # Select appropriate key for decryption 
            dchr = ord(echr) - key2  # Reverse decryption with key2
            decrypted_text = decrypted_text +chr(dchr)  # Add decrypted character to variable 
            key_sequence = key_sequence + 1  # Progress forward through key5 sequence

        elif key5 == "3":  # Select appropriate key for decryption 
            dchr = ord(echr) - key3  # Reverse decryption with key3
            decrypted_text = decrypted_text +chr(dchr)  # Add decrypted character to variable
            key_sequence = key_sequence + 1  # Progress forward through key5 sequence

        elif key5 == "4":  # Select appropriate key for decryption 
            dchr = ord(echr) - key4  # Reverse decryption with key4
            decrypted_text = decrypted_text +chr(dchr)  # Add decrypted character to variable
            key_sequence = key_sequence + 1  # Progress forward through key5 sequence

        elif key5 == "0":  # Select appropriate key for decryption 
            dchr = ord(echr) - 0  # No decryption required
            decrypted_text = decrypted_text +chr(dchr)  # Add unmodified character to variable
            key_sequence = key_sequence + 1  # Progress forward through key5 sequence  
    
    # Test mode
    #print(decrypted_text)  
    
    # Save decrypted text file    
    file_d = open("decrypted_text.txt", "w")
    file_d.write(str(decrypted_text))
    file_d.close
    

def verify():

    """Function to verify the decrypted_text file matches the raw_text file """

    file_r = open("raw_text.txt", "r")
    raw_text = file_r.read()

    file_d = open("decrypted_text.txt", "r")
    d_file = file_d.read()

    if raw_text == d_file:
        print("File verified!")

    else:
        print("Verification error!")

    
if __name__ == "__main__":    
    main()









