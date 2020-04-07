mu = 3.8
x0 = .5
S = 256
interval_min = .2
interval_max = .8
r = (interval_max - interval_min) / S


def f(xn):
    return mu * xn * (1 - xn)


# encrypt
x = x0
with open("files/textSample.txt", encoding="utf-8") as inFile:
    with open("files/encrypted.txt", "w") as outFile:
        while True:
            char = inFile.read(1)
            if not char:
                break
            # encrypt char by char
            x_min = interval_min + r * ord(char)
            x_max = interval_min + r * (ord(char) + 1)
            N = 0
            while x < x_min or x > x_max:
                x = f(x)
                N += 1
            outFile.write(str(N) + " ")

# decrypt
x = x0
# read encrypted N
with open("files/encrypted.txt") as inFile:
    numbers = inFile.readline().strip()
numbers = numbers.split(" ")

with open("files/decrypted.txt", "w", encoding="utf-8") as outFile:
    # decrypt N by N
    for N in numbers:
        for _ in range(int(N)):
            x = f(x)
        i = 0
        for i in range(S):
            if interval_min + r * i < x < interval_min + r * (i + 1):
                break
        outFile.write(chr(i))
