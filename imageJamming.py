# encrypt image but can decrypt because of modulo
# encrypted rgb values are the real ones
# takes too much time

import time

from PIL import Image

mu = 3.8
x0 = .5
S = 256
interval_min = .2
interval_max = .8
r = (interval_max - interval_min) / S


def f(xn):
    return mu * xn * (1 - xn)


fileName = input("file name: ")
start = time.time()
img = Image.open("files/" + fileName)
pix = img.load()
width, height = img.width, img.height

rgb = list()
enc_rgb = list()

for i in range(width):
    for j in range(height):
        rgb.append(pix[i, j])

x = x0
for triplet in rgb:
    pixel = list()
    for val in triplet:  # val is R then G the B
        x_min = interval_min + r * val
        x_max = interval_min + r * (val + 1)
        N = 0
        while x < x_min or x > x_max:
            x = f(x)
            N += 1
        pixel.append(N % S)
    enc_rgb.append(tuple(pixel))

encImage = Image.new(img.mode, (width, height))
encImage.putdata(enc_rgb)
encImage.save("files/enc_" + fileName)
print(time.time() - start)
