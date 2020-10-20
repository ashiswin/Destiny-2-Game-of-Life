from PIL import Image
import numpy as np
from skimage import io

im = Image.open("boards/85.tiff")
pix = im.load()
im2 = Image.open("boards - non-inverted/97.tiff")
pix2 = im2.load()

output = np.zeros(im.size, dtype=int)

for i in range(im.size[0]):
    for j in range(im.size[1]):
        output[i, j] = min(pix[i, j] + pix2[i, j], 1)

io.imsave("merged.tiff", output.transpose().astype(np.uint8) * 255)