"""
A program to add a "neon" effect to black-and-white photos
"""

from PIL import Image
from scipy.spatial import KDTree

img = Image.open('person.png')
im = img.load()

MAX_RADIUS = 20 # Light strength

dists = [[MAX_RADIUS] * img.size[1] for i in range(img.size[0])]

white_pixels = []
black_pixels = []

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if im[x, y] == (255, 255, 255, 255):
            white_pixels.append( (x, y) )
        else:
            black_pixels.append( (x, y) )

tree = KDTree(white_pixels)
results = tree.query(black_pixels)

for i in range(len(black_pixels)):
    x, y = black_pixels[i]
    dists[x][y] = results[0][i]

COLOR = (245, 0, 49)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if im[x, y] == (255, 255, 255, 255):
            continue
        RATIO = 1 - dists[x][y] / MAX_RADIUS
        im[x, y] = (int(RATIO * COLOR[0]), int(RATIO * COLOR[1]), int(RATIO * COLOR[2]), 255)

img.save('neon_person.png')