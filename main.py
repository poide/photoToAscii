import os

import imageProcessing
import cv2

def main():

    checkingPath = False
    while checkingPath==False:
        print("Please introduce the path to the photo")
        pathToPhoto = str(input())
        checkingPath = checkPath(pathToPhoto)

    pixelPadding = 0
    while pixelPadding <= 0:
        print("Please, introduce the pixel padding (factor to reduce the photo size):")
        temporalPixelPadding = input()
        if temporalPixelPadding.isnumeric():
            pixelPadding = int(temporalPixelPadding)


    imageProcessing.processImage(pixelPadding, pathToPhoto)

def checkPath(path):
    testOpen = cv2.imread(path)

    if testOpen is None:

        return False
    else:
        return True


if __name__ == "__main__":
    main()


