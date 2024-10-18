import cv2
from PIL import Image


image_path = 'dog.jpeg'

dog_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
dog_face = dog_face_cascade.detectMultiScale(image)


dog = Image.open(image_path)
glasses = Image.open('glasses.png')
for (x,y,w,h) in dog_face:
    glasses = glasses.resize((w, int(h / 3)))
    dog.paste(glasses, (x, int(y + h / 4)),glasses)
    dog.save("dog_with_glasses.png")
    dog_with_glasses = cv2.imread("dog_with_glasses.png")
    cv2.imshow("Dog_with_glasses", dog_with_glasses)
    cv2.waitKey()