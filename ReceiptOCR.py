import cv2
import pytesseract
from PIL import Image


filename = input("enter filename: ")
img=cv2.imread(filename)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
if "pre_processor"=="thresh":
    cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
if "pre_processor"=="blur":
    cv2.medianBlur(gray, 3)
      
cv2.imwrite("temp.png", gray)
text = pytesseract.image_to_string(Image.open("temp.png"))
print(text)
