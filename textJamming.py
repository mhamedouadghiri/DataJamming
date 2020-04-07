mu = 3.78
x0 = .5
S = 256
interval_min = .2
interval_max = .8
r = (interval_max - interval_min) / S


def f(xn):
    return mu * xn * (1 - xn)


msgToCrypt = "hello!"
encrypted = list()
decrypted = ""

# encrypt
x = x0
for char in msgToCrypt:
    x_min = interval_min + r * ord(char)
    x_max = interval_min + r * (ord(char) + 1)
    N = 0
    while x < x_min or x > x_max:
        x = f(x)
        N += 1
    encrypted.append(N)

print(msgToCrypt)
print(encrypted)

# decrypt
x = x0
for N in encrypted:
    for _ in range(N):
        x = f(x)
    i = 0
    for i in range(S):
        if interval_min + r * i < x < interval_min + r * (i + 1):
            break
    decrypted += chr(i)

print(decrypted)
