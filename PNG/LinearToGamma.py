import png
import numpy as np
reader = png.Reader('C:/png16.png')
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
    if bitdepth == 16:
        for i in range(0,row.size):
            if alpha and i%4 == 3:
                pass
            else:
                row[i] = pow(row[i]/65535,0.45)*255
    row = np.asarray(row,dtype='uint8')
    image.append(row)

f = open('C:/Test.png', 'wb')
writer = png.Writer(width, height, greyscale=greyscale,alpha=alpha)
writer.write(f, image)
f.close()

# import png
# import numpy as np

# reader = png.Reader('C:/png16.png')
# pngdata = reader.read()
# px_array = np.array( map( np.uint16, pngdata[2]))


# print(px_array.dtype)
# print(px_array.shape)