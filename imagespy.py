from PIL import Image

im = Image.open('doc.jpg')
w, h = im.size

w1 = w/3
h1 = h/4

# Facing Forward
im1 = im.crop((0, 0, w1, h1))
im2 = im.crop((w1, 0, w1*2, h1))
im3 = im.crop((w1*2, 0, w, h1))

# Left

im4 = im.crop((0, h1, w1, h1*2))
im5 = im.crop((w1, h1, w1*2, h1*2))
im6 = im.crop((w1*2, h1, w, h1*2))

# Right

im7 = im.crop((0, h1*2, w1, h1*3))
im8 = im.crop((w1, h1*2, w1*2, h1*3))
im9 = im.crop((w1*2, h1*2, w, h1*3))

# Back

im10 = im.crop((0, h1*3, w1, h))
im11 = im.crop((w1, h1*3, w1*2, h))
im12 = im.crop((w1*2, h1*3, w, h))

# im1.save("01.png")
# im2.save("02.png")
# im3.save("03.png")
# im4.save("04.png")
# im5.save("05.png")
# im6.save("06.png")
# im7.save("07.png")
# im8.save("08.png")
# im9.save("09.png")
# im10.save("10.png")
# im11.save("11.png")
# im12.save("12.png")
