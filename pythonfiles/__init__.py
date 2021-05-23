from PIL import Image
import math


# todo
def blur(img, radius):
    im = Image.open(img)
    imgcopy = Image.open(img)
    pixels2 = imgcopy.load()
    pixels = im.load()

    def checker(i, j):
        if (i < 0 or i >= im.size[0]) or (j < 0 or j >= im.size[1]):
            return False
        return True

    def average(xIndex, yIndex):
        # global radius
        red = 0
        blue = 0
        green = 0
        count = 0
        for i in range(xIndex - radius, xIndex + radius):
            for j in range(yIndex - radius, yIndex + radius):
                if checker(i, j):
                    red += pixels[i, j][0]
                    blue += pixels[i, j][1]
                    green += pixels[i, j][2]
                    count += 1
        red = int(red / count)
        green = int(green / count)
        blue = int(blue / count)
        return red, green, blue

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels2[i, j] = average(i, j);

    return imgcopy


# Image.open('cool.jpeg').show()
# pixelate('cool.jpeg',12).show()

def negative(img):
    im = Image.open(img)
    imgcopy = Image.open(img)
    pixels2 = imgcopy.load()
    pixels = im.load()

    def helper(i, j):
        red = 255 - pixels[i, j][0]
        green = 255 - pixels[i, j][1]
        blue = 255 - pixels[i, j][2]
        return red, green, blue

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels2[i, j] = helper(i, j)

    return imgcopy


def greyScale(img):
    im = Image.open(img)
    imgcopy = Image.open(img)
    pixels2 = imgcopy.load()
    pixels = im.load()

    def helper(i, j):
        red = pixels[i, j][0]
        green = pixels[i, j][1]
        blue = pixels[i, j][2]
        grey = int((red * 0.299) + (green * 0.587) + (blue * 0.114))
        return grey, grey, grey

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels2[i, j] = helper(i, j)

    return imgcopy


def saturationIncrease(img, saturation):
    im = Image.open(img)
    imgcopy = Image.open(img)
    pixels2 = imgcopy.load()
    pixels = im.load()

    def helper2(colors):
        dontMax = 0
        dontMin = 300
        for i in range(0, len(colors)):
            if colors[i] > dontMax:
                dontMax = colors[i]
            if colors[i] < dontMin:
                dontMin = colors[i]

        if saturation > 0:
            for i in range(0, len(colors)):
                if colors[i] == dontMax:
                    if colors[i] + saturation > 255:
                        colors[i] = 255
                    else:
                        colors[i] += saturation
                else:
                    colors[i] = colors[i] - saturation
                    if colors[i] < 0:
                        colors[i] = 0


        elif saturation < 0:

            ave = int(math.fsum(colors) / 3)
            difference = 300
            averageVala = colors[0]
            for itera in range(0, len(colors)):
                if int(math.fabs(colors[itera] - ave)) < difference:
                    difference = int(math.fabs(colors[itera] - ave))
                    averageVala = colors[itera]

            for i in range(0, len(colors)):
                if dontMin == colors[i]:
                    if colors[i] - saturation >= averageVala:
                        colors[i] = averageVala
                    else:
                        colors[i] -= saturation
                elif dontMax == colors[i]:
                    if colors[i] - math.fabs(saturation) <= averageVala:
                        colors[i] = averageVala
                    else:
                        colors[i] -= int(math.fabs(saturation))

        return colors[0], colors[1], colors[2]

    def helper(i, j):
        red = pixels[i, j][0]
        green = pixels[i, j][1]
        blue = pixels[i, j][2]
        return helper2([red, green, blue])

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels[i, j] = helper(i, j)

    return im


# Image.open('cool.jpeg').show()
# print(list(Image.open('ab.jpeg').getdata()))
# print(list(saturationIncrease('ab.jpeg', -4).getdata()))
# saturationIncrease('cool.jpeg', 20).show()


def colorize(img):
    im = Image.open(img)
    pixels = im.load()

    def helper2(colors):
        for i in range(0, len(colors)):
            if colors[i] < 85:
                colors[i] = 0
            elif colors[i] > 170:
                colors[i] = 255
        return colors[0], colors[1], colors[2]

    def helper(i, j):
        red = pixels[i, j][0]
        green = pixels[i, j][1]
        blue = pixels[i, j][2]
        return helper2([red, green, blue])

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels[i, j] = helper(i, j)

    return im


# Image.open('ab.jpeg').show()
# colorize('ab.jpeg').show()


def lighten(img, lighten):
    im = Image.open(img)
    pixels = im.load()

    def helper2(colors):
        for i in range(0, len(colors)):
            if colors[i] + lighten > 255:
                colors[i] = 255
            else:
                colors[i] += lighten
        return colors[0], colors[1], colors[2]

    def helper(i, j):
        red = pixels[i, j][0]
        green = pixels[i, j][1]
        blue = pixels[i, j][2]
        return helper2([red, green, blue])

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels[i, j] = helper(i, j)
    return im


def darken(img, dark):
    im = Image.open(img)
    pixels = im.load()

    def helper2(colors):
        for i in range(0, len(colors)):
            if colors[i] - dark < 0:
                colors[i] = 0
            else:
                colors[i] -= dark
        return colors[0], colors[1], colors[2]

    def helper(i, j):
        red = pixels[i, j][0]
        green = pixels[i, j][1]
        blue = pixels[i, j][2]
        return helper2([red, green, blue])

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels[i, j] = helper(i, j)
    return im


def pixelate(img, radius):
    im = Image.open(img)
    imgcopy = Image.open(img)
    pixels2 = imgcopy.load()
    pixels = im.load()

    def checker(i, j):
        if (i < 0 or i >= im.size[0]) or (j < 0 or j >= im.size[1]):
            return False
        return True

    for i in range(0, im.size[0] - radius, 2 * radius):  # for every pixel:
        for j in range(0, im.size[1] - radius, 2 * radius):
            for t in range(i - radius, i + radius):
                for k in range(j - radius, j + radius):
                    if checker(i, j):
                        pixels2[t, k] = pixels[i, j]

    return imgcopy





def yellosepia(img, quantity):
    im = greyScale(img)
    pixels = im.load()

    def helper(i, j):
        red = pixels[i, j][0]
        green = pixels[i, j][1]
        blue = pixels[i, j][2]

        if red + quantity > 255:
            red = 255
        else:
            red += quantity
        if green + quantity > 255:
            green = 255
        else:
            green += quantity

        return red, green, blue

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels[i, j] = helper(i, j)
    return im


def blueSepia(img, quantity):
    im = greyScale(img)
    pixels = im.load()

    def helper(i, j):
        red = pixels[i, j][0]
        green = pixels[i, j][1]
        blue = pixels[i, j][2]

        if blue + quantity > 255:
            blue = 255
        else:
            blue += quantity
        if green + quantity > 255:
            green = 255
        else:
            green += quantity

        return red, green, blue

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels[i, j] = helper(i, j)
    return im


def MixedSepia(img):
    im = Image.open(img)
    imgcopy = Image.open(img)
    pixels2 = imgcopy.load()
    pixels = im.load()

    def helper2(colors):
        colors[0] = int((0.393*colors[0])+(0.769*colors[1])+(0.189*colors[2]))
        colors[1] = int((0.349*colors[0])+(0.686*colors[1])+(0.168*colors[2]))
        colors[2] = int((0.272*colors[0])+(0.534*colors[1])+(0.131*colors[2]))
        return colors[0],colors[1],colors[2]

    def helper(i, j):
        red = pixels[i, j][0]
        green = pixels[i, j][1]
        blue = pixels[i, j][2]
        return helper2([red, green, blue])

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            pixels2[i, j] = helper(i, j)

    return imgcopy

Image.open('./sampleImages/cool.jpeg').show()
sepia('./sampleImages/cool.jpeg').show()