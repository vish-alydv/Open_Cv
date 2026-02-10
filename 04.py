import cv2

image = cv2.imread("download.jpeg")

if image is not None:
    h,w,c = image.shape
    print(f"Iamge loaded:\nHeight : {h} \n Width : {w} \n Channels: {c}")

else:
    print("Could Not Image ")