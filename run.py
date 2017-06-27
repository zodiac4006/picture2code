from PIL import Image
import math

if __name__ == '__main__':
	# 打开图片
	im = Image.open("1.jpg")
	# 将图片转为黑白模式
	im = im.convert("L")
	# 初始化压缩比
	rect_width = 8
	# 获得图片尺寸
	(width, height) = im.size
	# 压缩后图片宽度
	nwidth = math.ceil(width/rect_width)
	# 压缩后图片高度
	nheight = math.ceil(height/rect_width)
	# 获得图片数据
	lim = list(im.getdata())
	# 文件内容
	rect_list = []
	for i in range(0, nheight):
		for j in range(0, nwidth):
			sum_temp = 0
			for k in range(0, rect_width):
				x = (i*rect_width+k)*width+j*rect_width
				y = (i*rect_width+k)*width+j*rect_width + rect_width
				sum_temp += sum(lim[x: y])
			temp = math.ceil(sum_temp/(rect_width*rect_width))
			if temp > 255/3:
				rect_list.append("@@")
			else:
				rect_list.append("..")
		rect_list.append("\n")
	# 打开文件
	file_object = open('1.txt', 'w')
	# 写入内容
	file_object.write(''.join(rect_list))
	# 文件关闭
	file_object.close()
