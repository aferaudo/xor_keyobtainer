# How to cipher in python
import base64
import sys
import re


# cipher exor
def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key]))) 

def print_help():
    print("python3 cipher.py [plain_text] [hide_text_base64]")



def main (argv):

    if len(sys.argv) < 2:
        print_help()
        exit(0)

    print("############KEY OBTAINER XOR-CIPHER############\n\n")
    plain_text = sys.argv[1]
    print("Plain text received: " + plain_text)

    hide_text_base64 = sys.argv[2]
    print("Base64 received: " +  hide_text_base64)

    plain_text_bin = plain_text.encode()
    print("Plain text binary: " + plain_text_bin.decode())
    
    base64_ciph = base64.b64decode(hide_text_base64)
    print("First hide_text: " + str(base64_ciph))

    # Find key: Be careful! The key must be longer then plain text that you have to hide
    key_repeated = xor(base64_ciph, plain_text_bin)
    print("Key with repetition: " + str(key_repeated))
    
    # In this example key is qw8j

    # In this case key is to short, so we have to extend the key
    # For example we can do it manually, but we have to know how many
    # character we want to hide
    # key_tmp = key.decode() + "w"
    # print(key_tmp.encode())

    # Another solution could be: make the key much longer then the plain text.
    # So we have to choose a random length, but first find the charcater repetition in
    # the key.
    r = re.compile(r"(.+?)\1+")
    
    # Key without repetition
    key = min(r.findall(key_repeated.decode()) or [""], key=len)

    print("Key without repetition: " + str(key))

    print("\n\nNow you can use this key to make your own hide text\n\n")

    
if __name__ == '__main__':
    main(sys.argv)

