import imageProcessing
import cv2

def main():

    print("Please introduce the path to the photo")
    pathToPhoto = str(input())


    pixelPadding = 0
    while pixelPadding <= 0:
        print("Please, introduce the pixel padding (factor to reduce the photo size)")
        print("The pixel padding must be a number >= 1 using 1(to keep the same photo size)")
        pixelPadding = int(input())

    imageProcessing.processImage(pixelPadding, pathToPhoto)

if __name__ == "__main__":
    main()


