import cv2

image = cv2.imread("download.jpeg")


if image is None:
    print("Error Image Not Found")

else:
    print("Image Loaded Succesfully")