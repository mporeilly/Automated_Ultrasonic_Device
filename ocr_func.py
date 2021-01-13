## Place holder for OCR code that will allow the devices video output to be converted to 

#https://www.youtube.com/watch?v=kxHp5ng6Rgw&ab_channel=RatulDoley
#https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
import cv2
import pytesseract

im = Image.open('small.png')
text = pytesseract.image_to_string(im, lang="eng")   
print(text)
