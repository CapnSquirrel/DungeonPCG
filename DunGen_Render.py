from PIL import Image, ImageDraw

im = Image.new('RGBA', (400, 300), 'white')

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.show()
