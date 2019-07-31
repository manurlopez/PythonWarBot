import os
from PIL import Image, ImageDraw, ImageFont
import json

#Mira se un texto e JSOn e se o é leeo
def checkAndReadJson(data):
	try: dataJson = json.loads(data)
	except ValueError: return False
	return dataJson


def file_to_path(file_path):
	dirs = file_path.split("/")
	path = "/"
	num=len(dirs)-1
	for i in range(num):
		if len(dirs[i]) > 0:
			path = path + dirs[i] + "/"
	return path


def create_image(params_image,warDB):

	file_path = os.path.realpath(__file__)
	path = file_to_path(file_path)

	columns = params_image.get("columns") 
	marginLeft = params_image.get("marginLeft") 
	marginRight = params_image.get("marginRight") 
	marginTop = params_image.get("marginTop") 
	marginDown = params_image.get("marginDown") 
	spaceWith = params_image.get("spaceWith") 
	spaceHight = params_image.get("spaceHight") 
	font = params_image.get("font") 
	fontSize = params_image.get("fontSize") 

	#Creamos a imaxe collendo o numero de músicos e as filas necesarias
	numberPeople = warDB.people.count_documents({})
	ancho = marginLeft + (columns * spaceWith) + marginRight
	filas = (numberPeople // columns) + 1
	alto = marginTop + (filas * spaceHight) + marginDown
	img = Image.new('RGB', (ancho, alto), color = (255, 255, 255))
	d = ImageDraw.Draw(img)
	fnt = ImageFont.truetype(font, fontSize)

	#Variables auxiliares
	position = 0
	fila = 0

	#Recorremos tódolos músicos para poñelos na imaxe
	musicians = warDB.people.find({})
	for musician in musicians:
		if musician.get("alive") == 1 :
			d.text(((spaceWith * position) + marginLeft,(spaceHight * fila) + marginTop), musician.get("name"), font=fnt, fill=(0,255,0), align="center")
		else :
			d.text(((spaceWith * position) + marginLeft,(spaceHight * fila) + marginTop), musician.get("name"), font=fnt, fill=(255,0,0), align="center")
		position = position + 1
		if position == columns :
			fila = fila + 1
			position = 0

	#Gardamos a imaxe
	img.save(path + 'resume.png')


def remove_image():
	file_path = os.path.realpath(__file__)
	path = file_to_path(file_path)
	os.remove(path + "resume.png")









