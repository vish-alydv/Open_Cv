import cv2

image = cv2.imread("download.jpeg")


if image is None:
    print("Image is Not Loaded")


else:

    print("Image Loaded Succesfully")
    cv2.circle(image,(200,200),50 ,(255,0,0),-1)

    cv2.imshow("Circle On Image " ,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()