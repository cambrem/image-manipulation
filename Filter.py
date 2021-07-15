import cv2
import sys
import numpy as np

# get filename and filter from commandline
filename = sys.argv[1]
filter_ = sys.argv[2]

# read the image from the given file into img
img = cv2.imread('../' + filename)

# get the dimensions of the image (pixels)
dimensions = img.shape
h = dimensions[0]
w = dimensions[1]
# copy the original image into an image for filtering
filtered_img = cv2.resize(img, (w, h))

image = 'original'
cv2.namedWindow(image)
cv2.moveWindow(image, 0, 0)


for x in range(h):
    for y in range(w):
        if filter_ == 'sharpen':  # sharpen makes picture sharper on edges
            kernelSharpening = np.array([[9, -1, -1], [-1, -1, -1], [-1, -1, -1]])
            sharpen = cv2.filter2D(filtered_img, -1, kernelSharpening)
            cv2.imshow('Sharpened Image', sharpen)
            cv2.imshow(image, img)
            cv2.waitKey(0)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass
        elif filter_ == 'blur':  # normal blur uses average values of 7x7 window
            kernel_7x7 = np.ones((7, 7), np.float32)/49
            blurred = cv2.filter2D(img, -1, kernel_7x7)
            cv2.imshow('7x7_blurring', blurred)
            cv2.imshow(image, img)
            cv2.waitKey(0)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass
        elif filter_ == 'gaussianBlur':  # gaussian blur has more effect on the center of the image
            gBlur = cv2.GaussianBlur(img, (7, 7), 0)
            cv2.imshow('Gaussian blurring', gBlur)
            cv2.imshow(image, img)
            cv2.waitKey(0)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass
        elif filter_ == 'medianBlur':  # median blur blurs using the median of all elements
            mBlur = cv2.medianBlur(img, 5)
            cv2.imshow('median blurring', mBlur)
            cv2.imshow(image, img)
            cv2.waitKey(0)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass
        elif filter_ == 'bilateralBlur':  # bilateral blur keeps the edges sharp but blurs the photo
            bBlur = cv2.bilateralFilter(img, 9, 75, 75)
            cv2.imshow('bilateral blurring', bBlur)
            cv2.imshow(image, img)
            cv2.waitKey(0)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass
        elif filter_ == 'blue':  # sets color to blue
            cv2.imshow(image, img)
            lowerRange = np.array([25, 50, 50])
            upperRange = np.array([110, 255, 255])
            mask = cv2.inRange(img, lowerRange, upperRange)
            img[mask != 0] = [255, 0, 0]
            cv2.imshow('Blue Image', img)
            cv2.waitKey(0)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass
        elif filter_ == 'red':  # sets color to red
            cv2.imshow(image, img)
            lowerRange = np.array([160, 20, 70])
            upperRange = np.array([190, 255, 255])
            mask = cv2.inRange(img, lowerRange, upperRange)
            img[mask != 0] = [0, 0, 255]
            cv2.imshow('Red Image', img)
            cv2.waitKey(0)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass
        elif filter_ == 'green':  # sets color to green
            cv2.imshow(image, img)
            lowerRange = np.array([25, 50, 50])
            upperRange = np.array([110, 255, 255])
            mask = cv2.inRange(img, lowerRange,  upperRange)
            img[mask != 0] = [0, 255, 0]
            cv2.imshow('Green Image', img)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass

        elif filter_ == 'orange':  # sets color to orange
            cv2.imshow(image,img)
            lowerRange = np.array([160, 20, 70])
            upperRange = np.array([190, 255, 255])
            mask = cv2.inRange(img, lowerRange, upperRange)
            img[mask != 0] = [0, 179, 255]
            cv2.imshow('Orange Image', img)
            cv2.waitKey(0)
            while True:
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    exit()
            pass

image = 'Original Image'
cv2.namedWindow(image)
cv2.moveWindow(image, 0, 0)
cv2.imshow(image, img)

image = 'Filtered Image'
cv2.namedWindow(image)
cv2.moveWindow(image, 600, 0)
cv2.imshow(image, filtered_img)


# window will stay open until esc key is pressed
while True:
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        exit()
