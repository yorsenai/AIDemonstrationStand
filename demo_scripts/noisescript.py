import cv2
import numpy as np

def gauss_noise(image, mean=0, var=0.001):
    '''
        Добавить гауссовский шум
                 Среднее значение: среднее
                 Вар: Разнообразие
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)

    return out


def noiseattack(image : str, level : str = "low"):
	try:
		img = cv2.imdecode(np.fromfile(image, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
		
		if "high" in level:
			mean = -0.15
		else:
			mean = 0

		# Добавить гауссовский шум, среднее значение 0, а дисперсия составляет 0,01
		noised_img = gauss_noise(img, mean=mean, var = 0.0005)

		new_name = image[7 : image.find(".p")]
		cv2.imencode(".png", noised_img)[1].tofile("pics\\" + new_name + "_out.png")

		return True
	except:
		return False