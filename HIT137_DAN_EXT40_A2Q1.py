"""
Hit137: Team Dan_Ext40

Assessment 2: Question 1

Program: Ass2_Q1.py

Authors: Maharun Momo Islam, Moneya Islam, Andrew Morris, Kudzaishe Mutyasira
Last date modified: 30/08/25

Encryption / Decryption:
The purpose of this program is to accept two shift numbers from the user and 
use these to create four keys that will shift the characters up or down 
depending on their case and position in the alphabet. 
encrypt a text file and save it, load that file decrypt it, and save it. It 
will then load the original text file and verify that it matches the 
decrypted file.

"""

shift1 = int (input("Please enter first shift number: "))
shift2 = int (input("Please enter second shift number: "))

key1 = shift1 * shift2
key2 = - shift1 + - shift2
key3 = - shift1
key4 = shift2 ** 2

def main():
    """The main function of this program"""
        
    """Show keys"""
    print (key1, key2, key3, key4)  # Test mode 
   
    """Encrypt the raw_text"""
    encrypt()    
        
    print ("File encrypted!")
    print ("Encrypted text file saved.")
    
    """Decrypt the encrypted_text"""
    decrypt()

    print ("File decrypted!")
    print ("Decrypted text file saved.")

    """Compare decrypted_text"""
    verify()


    """Define functions"""

def encrypt():
    """Function to encrypt the raw_txt file and save as encrypted_text.txt"""

    file_raw = open ("raw_text.txt", "r")
    raw_text = file_raw.read()

    encrypted_text = ""
    key_text = ""
    for ch in raw_text:
        if ch >= chr(97) and ch <= chr(109):
            echr = ord(ch) + key1
            encrypted_text = encrypted_text + chr(echr)
            key_text = key_text + "1"
        elif ch >= chr(110) and ch <= chr(122):
            echr = ord(ch) + key2
            encrypted_text = encrypted_text + chr(echr)
            key_text = key_text + "2"
        elif ch >= chr(65) and ch <= chr(77):
            echr = ord(ch) + key3
            encrypted_text = encrypted_text + chr(echr)
            key_text = key_text + "3"
        elif ch >= chr(78) and ch <= chr(90):
            echr = ord(ch) + key4
            encrypted_text = encrypted_text + chr(echr)
            key_text = key_text + "4"
        else:
            encrypted_text = encrypted_text + ch
            key_text = key_text + "0"

    """ Test to compare input and output"""
    print (raw_text)  # Test mode
    print (encrypted_text)  # Test mode
    print (key_text)  # Test mode

    """Save encrypted file"""
    
    file_e = open ("encrypted_text.txt", "w", encoding = "utf-8")
    file_e.write (str(encrypted_text))
    file_e.close
    file_e = open ("key_text.txt", "w")
    file_e.write (str(key_text))
    file_e.close     
        
def decrypt():
    """Function to decrypt the encrypted_text file"""

    file_e = open ("encrypted_text.txt", "r", encoding = "utf-8")
    etext = file_e.read()
    file_e = open ("key_text.txt", "r")
    ktext = file_e.read()
    print ("Encrypted text file loaded")
    
    print (etext)  # Test mode
    
    decrypted_text = ""
    y = 0

    for echr in etext:
        x = ktext[y]
        if x == "1":
            dchr = ord(echr) - key1
            decrypted_text = decrypted_text +chr(dchr)
            y = y + 1
        elif x == "2":
            dchr = ord(echr) - key2
            decrypted_text = decrypted_text +chr(dchr)  
            y = y + 1
        elif x == "3":
            dchr = ord(echr) - key3
            decrypted_text = decrypted_text +chr(dchr) 
            y = y + 1
        elif x == "4":
            dchr = ord(echr) - key4 
            decrypted_text = decrypted_text +chr(dchr) 
            y = y + 1
        elif x == "0":
            dchr = ord(echr) - 0
            decrypted_text = decrypted_text +chr(dchr) 
            y = y + 1    
    
    print (decrypted_text)   

    """ Test to compare input and output"""

    print (decrypted_text)  # Test mode

    """Save decrypted file"""
    
    file_d = open ("decrypted_text.txt", "w")
    file_d.write (str(decrypted_text))
    file_d.close

    

def verify():
    """Function to verify the decrypted_text file matches the raw_text file """

    file_r = open ("raw_text.txt", "r")
    raw_text = file_r.read()

    file_d = open ("decrypted_text.txt", "r")
    d_file = file_d.read()

    if raw_text == d_file:
        print ("File verified!")
    else:
        print ("Verification error!")
    
main()









