"""
Hit137: Team Dan_Ext40
Assessment 2: Question 1
"""

def main():

    """The main function of this program"""

    shift1 = int (input("Please enter first shift number: "))
    shift2 = int (input("Please enter second shift number: "))

    key1 = shift1 * shift2
    key2 = - shift1 + - shift2
    key3 = - shift1
    key4 = shift2 ** 2
    
    print (key1, key2, key3, key4) # Test mode
      
    """Encrypt the raw_text"""
    
    encrypt()

    """Decrypt the encrypted_text"""
    
    decrypt()

    """Compare decrypted_text"""
    
    verify()

def encrypt():

    """Function to encrypt the raw_txt file"""

    f = open ("raw_text.txt", "r")
    raw_text = f.read()

    print (raw_text) # Test mode
    
    return

def decrypt():

    """Function to decrypt the encrypted_text file"""

    return

def verify():

    """Function to verify the decrypted_text file matches the raw_text file """

    return

main()





