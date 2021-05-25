# PYSVAP Image Processing Python Library

## Details:
* Python library which manipulates individual pixels' rgb values in order to return required results.
* Created using python PILLOW library.
* Implements 14 functions with modifiable intensity

## Methods:
1. gaussianBlur(imgSource,Radius):
* imgSource is the link of the image location
* Returns the blurred image with the radius you would want to blur the image with.
* Greater the radius, more blurred the image will be.

2. negative(imgSource):
* imgSource is the link of the image location
* Returns the negative of an image. 

3. grayScale(imgSource):
* imgSource is the link of the image location
* Returns the grayScale(black and white) of an image. 

4. saturation(imgSource, saturate):
* imgSource is the link of the image location
* saturate is the intensity by which you want to saturate the image. Use saturate values from 1 - 3 to increase saturation. Use saturate values from 0 to 1 to decrease saturation values. The saturate argument can be of float type.
* returns a saturated or desaturated image based on saturated value passed in the method.!

5. posterize(imgSource):
* imgSource is the link of the image location
* posterizes the image and returns the result
* returns a posterized image

6. lighten(imgSource,lighten):
* imgSource is the link of the image location
* lighten is the intensity by which you would want to increase the lightness of the image. It can have values from 0 to 255.
* returns a lightened image

7. darken(imgSource,darken):
* imgSource is the link of the image location
* darken is the intensity by which you would want to decrease the lightness of the image. It can have values from 0 to 255.
* returns a darken image

8. pixelate(imgSource,radius):
* imgSource is the link of the image location
* Returns the pixelated image with the radius you would want to blur the image with.
* Greater the radius, more pixelated the image will be.
* runs in linear time

9. yellowsepia(imgSource,intensity):
* imgSource is the link of the image location
* darken is the intensity by which you would want to increase the intensity of the sepia effect. It can have values from 0 to 255.
* returns a yellowSepia image

10. blueSepia(imgSource,intensity):
* imgSource is the link of the image location
* darken is the intensity by which you would want to increase the intensity of the sepia effect. It can have values from 0 to 255.
* returns a blueSepia image

11. mixedSepia(imgSource):
* imgSource is the link of the image location
* returns a mixed sepia image with values of both yellow sepia and blue sepia

12. temperature(imgSource, tempVal):
* imgSource is the link of the image location
* tempVal is the intensity by which you can either increase the temperature or decrease the temperature of the image. It can have both positive and negative values. From 0 to 255 and from -255 to 0.
* for positive values, adds a yellow tint on the image, for negative values, adds a bluish tint
* returns an image with either a yellow tint or a blue tint.

13. overLay(img,color,intensity):
* imgSource is the link of the image location
* color is the color of overall you want on your image. It can be off the following types:    
    red,green,blue,yellow,orange,violet
* intensity provides information on extent of overlay. Can be between 0 and 255
* returns an image with a overlay on top

14. colorShift(img,num):
* imgSource is the link of the image location
* num is the colorshift option you can choose. It can be from 1 - 5.
* returns an image with colorshifted pixels.











Copyright 2021 SHUBH VASHISHT and AMAN PRIYADARSHI

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.