
import png
import numpy as np
import sys
import os


def GammaTranslateAlpha(pngPath,savePath):
    reader = png.Reader(pngPath)
    data = reader.asDirect()
    width = data[0]
    height = data[1]
    pixels = data[2]
    greyscale = data[3]['greyscale']
    alpha = data[3]['alpha']
    bitdepth = data[3]['bitdepth']
    image = []
    i = 0
    j = 0
    for row in pixels:
        row = np.asarray(row)
        if bitdepth == 8:
            for i in range(0,row.size):
                if alpha and i%4 == 3:
                    row[i] = pow(row[i]/255,2.2)*255
                    
        row = np.asarray(row,dtype='uint8')
        image.append(row)

    f = open(savePath, 'wb')
    writer = png.Writer(width, height, greyscale=greyscale,alpha=alpha)
    writer.write(f, image)
    f.close()

if __name__ == "__main__":
    path = sys.argv[1]
    savePath = sys.argv[2]
    if not os.path.isdir(savePath):
        os.makedirs(savePath)
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for onedir in dirs:
                saveDir = os.path.join(root,onedir).replace(path,savePath)
                if not os.path.isdir(saveDir):
                    os.makedirs(saveDir)
            for onefile in files:
                oneFileSavePath = os.path.join(root,onefile).replace(path,savePath)
                GammaTranslateAlpha( os.path.join(root,onefile),oneFileSavePath)
    else:
        pass

    pass
