import sys

# baptista constants
mu = 3.8
x0 = .5
S = 256
interval_min = .2
interval_max = .8
r = (interval_max - interval_min) / S

file_name = sys.argv[1]

# read the contents of the file
with open("files/" + file_name, "r", encoding="utf-8") as file:
    text = file.readlines()

# to store the encrypted text
text_encrypted = []

# baptista 
x = x0
for line in text:
    result = ""
    for i in range(len(line)):
        char = line[i]
        if char.isspace():
            result += char
            continue
        
        x_min = interval_min + r * ord(char)
        x_max = interval_min + r * (ord(char) + 1)
        N = 0
        while x < x_min or x > x_max:
            x = mu * x * (1 - x)
            N += 1
        
        if chr(N).isspace():
            result += chr(256)
        else:
            result += chr(N)
    
    text_encrypted.append(result)

# write to encryption file
with open("files/encrypted_" + sys.argv[1], "w", encoding="utf-8") as file:
    file.writelines(text_encrypted)