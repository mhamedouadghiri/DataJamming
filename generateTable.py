mu = 3.8
x0 = 0.5
S = 256  # the whole extended ascii table
x_min = 0.2
x_max = 0.9
r = (x_max - x_min) / S


def f(xn):
    return mu * xn * (1 - xn)


table = dict()
setOfCodes = set()
for asciiCode in range(0, 256):
    r_min = x_min + r * asciiCode
    r_max = x_min + r * (asciiCode + 1)
    x = x0
    N = 0

    while x >= r_max or x <= r_min:
        x = f(x)
        N += 1

    char = chr(asciiCode)
    table[char] = N
    setOfCodes.add(N)

# print(table)

# S = 256 so the length of the set where we add the coded number
# should be 256 so each character has a unique code
# it is somewhat a verification that the initial conditions work
# print(len(setOfCodes))  # must be = 256
