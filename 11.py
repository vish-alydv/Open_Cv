import cv2

image = cv2.imread("download.jpeg")


if image is None:
    print("Image is Not Loaded")


else:

    print("Image Loaded Succesfully")

    # pt1 =(50,100)

    # pt2 = (100,200)

    # color  =(0,4,255)

    # thickness = 4

    cv2.rectangle(image ,pt1 =(50,100),pt2 = (100,200), color=(0,4,255) ,thickness =4)

    cv2.imshow("Image With Line",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows