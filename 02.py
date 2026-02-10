import cv2

image = cv2.imread("download.jpeg")


if image is not None:
    cv2.imshow("The Image" ,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image Not Loaded Succesfully")