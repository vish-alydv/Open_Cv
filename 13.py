import cv2

image = cv2.imread("download.jpeg")


if image is None:
    print("Image is Not Loaded")


else:

    print("Image Loaded Succesfully")

    cv2.putText(image ," Sample " ,(200,200), cv2.FONT_ITALIC , 1.8 , (255,0,0),2)

    cv2.imshow("Text On Image" ,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()