import sys

def cipher(message, key):
    result = ""
    for i in range(len(message)):
        chr1 = message[i]
        
        if chr1.isspace():
            result += chr1
            continue
        
        chr2 = key[i % len(key)]
        r = chr(ord(chr1) ^ ord(chr2))
    
        if r.isspace():
            result += chr(256)
        else:
            result += r
        
    return result


message = sys.argv[1]
try:
	key = sys.argv[2]
except:
	key = "pfa2020"

result = cipher(message, key)

print("\n")
print("Message:", message)
print("Key:", key)
print("Encrypted message:", result)
print("\n")
