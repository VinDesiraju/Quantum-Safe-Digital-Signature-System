# imports
from cryptovinaigrette import cryptovinaigrette
from datetime import datetime as dt

__RED = "\033[0;31m"     # ANSI escape code for red text in terminal
__GREEN = "\033[0;32m"   # ANSI escape code for green text
__NOCOLOR = "\033[0m"    # ANSI escape code for resetting the text color back to the default


def colored_binary(b):
    if b:
        return __GREEN + str(b) + __NOCOLOR
    else:
        return __RED + str(b) + __NOCOLOR


class args: pass


args = args()
args.v = True

if __name__ == '__main__':
    # generating keys
    myKeyObject = cryptovinaigrette.rainbowKeygen(save='./')

    # signing the document using the private key file generated in the same directory
    start = dt.now()
    signature = cryptovinaigrette.rainbowKeygen.sign('Priv.pem', 'realDog.txt')
    end = dt.now()
    if args.v:
        print()
        print("Signed (from file) in", end - start, "seconds")

    # verifying the signed document using the public key file generated in the same directory
    print()
    print("Checking realDog.txt")
    start = dt.now()
    print("Signature verification with file:",
          colored_binary(cryptovinaigrette.rainbowKeygen.verify('Pub.pub', signature, 'realDog.txt')))
    end = dt.now()
    if args.v:
        print("Verified signature in", end - start, "seconds")

    # Now, signing the document using the private key from the key object we initialized
    start = dt.now()
    signature = cryptovinaigrette.rainbowKeygen.sign(myKeyObject.private_key, 'realDog.txt')
    end = dt.now()
    if args.v:
        print()
        print("Signed (from key object) in", end - start, "seconds")

    # verifying the signed document using the public key from the key object we initialized
    print()
    print("Checking realDog.txt")
    start = dt.now()
    print("Signature verification with object :",
          colored_binary(cryptovinaigrette.rainbowKeygen.verify(myKeyObject.public_key, signature, 'realDog.txt')))
    end = dt.now()
    if args.v:
        print("Verified signature in", end - start, "seconds")

    if args.v >= 2:
        print("Signature :", signature)

    # verifying a different document using the public key
    print()
    print("Checking fakeDog.txt")
    start = dt.now()
    print("Signature verification with tampered file :",
          colored_binary(cryptovinaigrette.rainbowKeygen.verify('Pub.pub', signature, 'fakeDog.txt')))
    end = dt.now()
    if args.v:
        print("Verified signature in", end - start, "seconds")

    if args.v >= 2:
        print("Signature :", signature)
