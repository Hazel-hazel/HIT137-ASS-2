"""
Hit137: Team Dan_Ext40
Assessment 2: Question 1
"""

def main():
    """The main function of this program"""

    shift1 = int (input("Please enter first shift number: "))
    shift2 = int (input("Please enter second shift number: "))

    f = open ("raw_text.txt", "r")
    key1 = shift1 * shift2
    key2 = - shift1 + - shift2
    key3 = - shift1
    key4 = shift2 ** 2

    f = open ("raw_text.txt", "r")
    raw_text = f.read()
    
    print (raw_text) # Test mode
    print (key1, key2, key3, key4) # Test mode

def encrypt():
    """Encrypts the raw_txt file"""

    return

def decrypt():
    """Decrypts the encrypted_text file"""
    return

def verify():
    """Verifys the decrypted_text file with the raw_text file """

    return


main()


