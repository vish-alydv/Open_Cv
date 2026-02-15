import cv2

image = cv2.imread("download.jpeg")


if image is None:
    print("Image is Not Loaded")


else:

    print("Image Loaded Succesfully")

    pt1 =(50,100)

    pt2 = (100,200)

    color  =(255,0,0)

    thickness = 4

    cv2.line(image ,pt1 ,pt2 ,color ,thickness)

    cv2.imshow("Image With Line",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows