from PIL import Image


im = Image.open("1.jpg")
im = im.convert("L")
(width, height) = im.size
nwidth = width/10
nheight = height/10
lim = list(im.getdata())
for line in range(0, width*height, width):
	print(lim[line:line+width])
	

