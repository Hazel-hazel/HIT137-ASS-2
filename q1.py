# q1 Encrypt and Decrypt a file using shifts

def encrypt(text, s1, s2):
    result = ""
    for ch in text:
        if ch.isLower(): # lowercase rule
            if ch <= "m": 
                result = result + chr((ord(ch) - ord("a") + s1 * s2) % 13 + ord("a")) # first half of alphbet a-m
            else:          
                result = result + chr((ord(ch) - ord("n") - (s1 + s2)) % 13 + ord("n")) # second half of aplabet n-z
        elif ch.isUpper(): # uppercase rule
            if ch <= "M":  
                result = result + chr((ord(ch) - ord("A") - s1) % 13 + ord("A")) # first half A-M
            else:          
                result = result + chr((ord(ch) - ord("N") + (s2 ** 2)) % 13 + ord("N")) # seond half N-Z
        else:
            result = result + ch
    return result