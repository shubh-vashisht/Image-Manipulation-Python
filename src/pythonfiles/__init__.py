from PIL import Image
from src.functions.blur import gaussianBlur
from src.functions.negative import negative
from src.functions.grayScale import grayScale
from src.functions.saturate import saturation
from src.functions.posterize import posterize
from src.functions.lighten import lighten
from src.functions.darken import darken
from src.functions.pixelate import pixelate
from src.functions.sepia import yellowsepia
from src.functions.sepia import blueSepia
from src.functions.sepia import MixedSepia
from src.functions.temp import temperature
from src.function.overlay import overLay
from src.functions.colorShift import colorShift


Blur = gaussianBlur
neg = negative
gray = grayScale
sat = saturation
post = posterize
lightn = lighten
darkn = darken
pixel8 = pixelate
ysepia = yellowSepia
bsepia = blueSepia
msepia = MixedSepia
temp = temperature
overLay = overLay
colorShift = colorShift

# pixel8('/Users/shubh/PycharmProjects/ImageManipulation/sampleImages/4f503844d9a44b0350c25eeefae028d3.jpeg',50).show()


pixel8("/Users/shubh/PycharmProjects/ImageManipulation/sampleImages/shubh.jpg", 50).show()
