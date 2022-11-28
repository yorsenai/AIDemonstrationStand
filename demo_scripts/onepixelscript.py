from PIL import Image
from random import randint

def onepixattack(image : str):
	try:
		im = Image.open(image)
		pixelMap = im.load()
		
		img = Image.new( im.mode, im.size)
		pixelsNew = img.load()

		for i in range(img.size[0]):
			for j in range(img.size[1]):
				pixelsNew[i,j] = pixelMap[i,j]
		pixelsNew[randint(10, 18), randint(10, 18)] = (255,0,0,255)


		im.close()
		#new_name = image[7 : image.find(".p")]
		new_name = image.replace(".png", "")
		print(new_name)
		img.save(new_name + "_out.png", "PNG")
		img.close()

		return True
	except:
		return False