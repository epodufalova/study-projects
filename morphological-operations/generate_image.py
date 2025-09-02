import random
from PIL import Image

width, height = 256, 256

image = Image.new('L', (width, height))

for y in range(height):
    for x in range(width):
        gray_value = random.randint(0, 255)
        image.putpixel((x, y), gray_value)

image.save("random_gray.bmp")
