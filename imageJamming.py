# encrypts image but cannot decrypt because of modulo
# takes too much time (3min for 512*512px, 30sec for 256*256px)

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

# extract RGB values and store them in rgb list
for i in range(width):
    for j in range(height):
        rgb.append(pix[i, j])

# encryption
x = x0
for triplet in rgb:
    pixel = list()
    for val in triplet:  # val is R then G the B for each pixel
        x_min = interval_min + r * val
        x_max = interval_min + r * (val + 1)
        N = 0
        while x < x_min or x > x_max:
            x = f(x)
            N += 1
        # problem of losing data here, when storing modulo of encrypted RGB values
        pixel.append(N % S)
    enc_rgb.append(tuple(pixel))

# save encrypted image
encImage = Image.new(img.mode, (width, height))
encImage.putdata(enc_rgb)
encImage.save("files/enc_" + fileName)

print(time.time() - start)
