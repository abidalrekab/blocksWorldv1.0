# https://pypi.org/project/Pillow/
# https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?highlight=draw

from PIL import Image, ImageDraw
import math

def drawText(canvas, taskList):
    for task in taskList:
        char = task[0]
        coordinates = task[1]

        canvas.text(coordinates, char)

def regularTriangle(x, y, size):
    output = []

    x0 = x
    y0 = y - int(size / math.sqrt(3.0))
    output.append((x0, y0))

    x1 = x - int(size / 2.0)
    y1 = y + int(size / math.sqrt(3.0) / 2.0)
    output.append((x1, y1))

    x2 = x + int(size / 2.0)
    y2 = y + int(size / math.sqrt(3.0) / 2.0)
    output.append((x2, y2))

    return output

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileName = 'text.png'

image = Image.new(imageMode, imageSize, imageBackground)

taskList = [
    ['+', (5,  5)],
    ['+', (5, 15)],
    ['+', (5, 25)],
    ['+', (5, 35)],
    ['+', (5, 45)],
    ['+', (5, 55)],
    ['+', (5, 65)],
    ['+', (5, 75)],
]

canvas = ImageDraw.Draw(image)

drawText(canvas, taskList)

taskList = []
for point in regularTriangle(320, 240, 50):
    taskList.append(['+', point])

drawText(canvas, taskList)

image.save(fileName, fileType)