import cv2

image = cv2.imread("download.jpeg")


if image is None:
    print("Image is Not Loaded")


else:
    flipped_horizontal = cv2.flip(image , 1)
    flipped_vertical = cv2.flip(image , 0)
    flipped_vertical_horizontal = cv2.flip(image , -1)

    cv2.imshow("Original Image" , image)
    cv2.imshow("Horizontal Flip" ,flipped_horizontal)
    cv2.imshow("Vertical Flip" ,flipped_vertical)
    cv2.imshow("Horizontal - Vertical Flip" , flipped_vertical_horizontal)


    cv2.waitKey(0)
    cv2.destroyAllWindows()