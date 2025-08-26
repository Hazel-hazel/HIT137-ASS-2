"""
Hit137: Team Dan_Ext40
Assessment 2: Question 1
"""

shift1 = int (input("Please enter first shift number: "))
shift2 = int (input("Please enter second shift number: "))

key1 = shift1 * shift2
key2 = - shift1 + - shift2
key3 = - shift1
key4 = shift2 ** 2

raw_text = ""
e_text = ""
    

def main():
    """The main function of this program"""
        
    """Show keys"""
    print (key1, key2, key3, key4) # Test mode 
   
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

    file_r = open ("raw_text.txt", "r")
    raw_text = file_r.read()

    e_text = ""

    for ch in raw_text:
        echr = ord(ch) + key2
        e_text = e_text + chr(echr)

    """ Test to compare input and output"""
    print (raw_text) # Test mode
    print (e_text) # Test mode

    """Save encrypted file"""
    
    file_e = open ("encrypted_text.txt", "w")
    file_e.write (str(e_text))
    file_e.close
          
    return

def decrypt():
    """Function to decrypt the encrypted_text file"""

    file_e = open ("encrypted_text.txt", "r")
    enc_text = file_e.read()

    d_text = ""

    for ech in enc_text:
        echr = ord(ech) - key2
        d_text = d_text + chr(echr)

    """ Test to compare input and output"""
    print (enc_text) # Test mode
    print (d_text) # Test mode

    """Save decrypted file"""
    
    file_d = open ("decrypted_text.txt", "w")
    file_d.write (str(d_text))
    file_d.close
    return

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
    return

main()











