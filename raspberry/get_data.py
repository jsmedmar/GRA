import time
import picamera
import pygame.camera
import pygame.image
import get_weight
import requests

def take_ir():
	with picamera.PiCamera() as camera:
		camera.start_preview()
		time.sleep(1)
		camera.capture('ir.jpg')
		camera.stop_preview()

def take_color():
	pygame.camera.init()
	cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
	cam.start()
	img = cam.get_image()
	pygame.image.save(img, "color.jpg")
	pygame.camera.quit()

take_ir()
take_color()

data = {'ecan':'1', 'weight':get_weight.get()}
files = {'image_color': open('color.jpg', 'rb'),'image_ir':open('ir.jpg', 'rb')}
#url = 'http://127.0.0.1:8000/ecan/upload/'
url = 'http://ecan-recognition.herokuapp.com/ecan/upload/'
r = requests.post(url, data = data, files=files)

print get_weight.get()
print r.text
