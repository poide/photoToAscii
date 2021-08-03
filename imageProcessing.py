import cv2
import os.path
def processImage(pixelPadding,pathToPhoto):
    imageName = os.path.basename(pathToPhoto)
    image = cv2.imread("/home/pepe/Downloads/image.jpg")
    height, width, channels = image.shape
    aspectRatio = height/width
    pixelPaddingHeight = pixelPadding
    pixelPaddingWidth= int(pixelPaddingHeight*aspectRatio)
    pixelPerRectangle = pixelPaddingWidth*pixelPaddingHeight
    f = open("output/"+ imageName + ".txt", "w+")
    f.write(processFrame(width, height, image, pixelPaddingWidth, pixelPaddingHeight, pixelPerRectangle))
    f.close()


def processFrame(width, height, image,pixelPaddingWidth,pixelPaddingHeight,pixelPerRectangle):
    gradient = "@%#*+=-:.  "
    yStartPosition = 0
    res = ""

    while yStartPosition + pixelPaddingHeight < height:
        xStartPosition = 0
        while xStartPosition + pixelPaddingWidth < width:
            sumaRojo,sumaVerde,sumaAzul = 0,0,0
            for i in range(pixelPaddingWidth):
                for j in range(pixelPaddingHeight):
                    sumaRojo, sumaVerde, sumaAzul  = sumaRojo + image[yStartPosition + j][xStartPosition + i][0],sumaVerde + image[yStartPosition + j][xStartPosition + i][1],sumaAzul + image[yStartPosition + j][xStartPosition + i][2]
            medRojo,medVerde,medAzul = sumaRojo/(pixelPerRectangle), sumaVerde/(pixelPerRectangle), sumaAzul/(pixelPerRectangle)
            luminosity = (0.3 * medRojo) + (0.59 * medVerde ) + (0.11 * medAzul)
            asciiCharacter = gradient[int(((len(gradient)-1)/255)*luminosity)]
            res = res + asciiCharacter + " "
            xStartPosition = xStartPosition + pixelPaddingWidth
        yStartPosition = yStartPosition + pixelPaddingHeight
        res = res + "\n"
    return res

