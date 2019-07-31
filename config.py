import json
import utilities
import os

class Config:

	def __init__(self):

		#Collemos o archivo 
		file_path = os.path.realpath(__file__)
		path = utilities.file_to_path(file_path)
		fileName = path + "config.json"
		
		#Por defecto o arquivo de configuración está mal
		self.correctConfig = -1

		#Se o arquivo non existe salimos do método
		if (not os.path.isfile(fileName)): return

		#Abrimos o ficheiro e lemos tóda a información
		file = open(fileName,"r")
		fileData = file.read()

		#Comrpobamos que a información e un json e cerramolo arquivo
		data = utilities.checkAndReadJson(fileData)
		file.close()
		if(not data): return

		#Comrpobamos que ten tódalas claves que son necesarias
		if not self.jsonCorrecto(data): return

		#Cargamos a información da base de datos sempre e cando os datos sexan do tipo correcto
		database = data.get("database")
		self.db = {}
		if isinstance(database.get("url"), str) == False: return
		if isinstance(database.get("port"), str) == False: return 
		if isinstance(database.get("name"), str) == False: return 
		if isinstance(database.get("user"), str) == False: return 
		if isinstance(database.get("password"), str) == False: return 
		self.db.update({"url" : database.get("url")})
		self.db.update({"port" : database.get("port")})
		self.db.update({"name" : database.get("name")})
		self.db.update({"user" : database.get("user")})
		self.db.update({"password" : database.get("password")})

		#Cargamos o que ten que ver con twitter
		twitter = data.get("twitter")
		if isinstance(twitter.get("consumer key"), str) == False: return
		if isinstance(twitter.get("consumer secret"), str) == False: return
		if isinstance(twitter.get("access token"), str) == False: return
		if isinstance(twitter.get("access token secret"), str) == False: return
		self.consumer_key = twitter.get("consumer key")
		self.consumer_secret = twitter.get("consumer secret")
		self.access_token = twitter.get("access token")
		self.access_token_secret = twitter.get("access token_secret")	

		#Collemos o ano de empezar
		if isinstance(data.get("year to start"), int) == False: return
		self.year_start = data.get("year to start")

		#Collemos a información da imaxe
		self.image = {}
		self.image.update({"columns" : 5 })
		self.image.update({"marginLeft" : 20 })
		self.image.update({"marginRight" : 20 })
		self.image.update({"marginTop" : 15 })
		self.image.update({"marginDown" : 5 })
		self.image.update({"spaceWith" : 140 })
		self.image.update({"spaceHight" : 40 })
		self.image.update({"font" : path + '/' +'DejaVuSans-Bold.ttf' })
		self.image.update({"fontSize" : 15 })

		#Collemos a configuración do texto
		text = data.get("text")
		self.text = {}
		if isinstance(text.get("lenguage"), str) == False: return
		if isinstance(text.get("people"), str) == False: return
		if isinstance(text.get("hashtag"), str) == False: return
		self.text.update({"lenguage" : text.get("lenguage")})
		self.text.update({"people" : text.get("people")})
		self.text.update({"hashtag" : text.get("hashtag")})

		#Collemos as horas que hai unha morte comprobando que son enteiros
		if isinstance(data.get("hours to kill"), list) == False: return
		hours = data.get("hours to kill")
		self.hours = []
		for hora in hours :
			if isinstance(hora, int): self.hours.append(hora)
		if len(self.hours) == 0 : return


		#Collemos o usuario do sistema
		if isinstance(data.get("pc user"), str) == False: return
		self.pc_user = data.get("pc user")

		#Cargouse a configuracion corrrectamente
		self.correctConfig = 1

	def jsonCorrecto(self,data):

		# Comrpobamos que estan tódolos datos da base de datos
		if "database" not in data: return False
		else:
			db = data.get("database")
			if "url" not in db: return False
			if "port" not in db: return False
			if "name" not in db: return False
			if "user" not in db: return False
			if "password" not in db: return False

		#Comrpobamos que estan tódolos datos correspondentes a twitter
		if "twitter" not in data: return False
		else:
			twitter = data.get("twitter")
			if "consumer key" not in twitter: return False
			if "consumer secret" not in twitter: return False 
			if "access token" not in twitter: return False
			if "access token secret" not in twitter: return False

		#Comrpobamos que está o ano en que se empeza
		if "year to start" not in data: return False

		#Comrpobamos que está o texto que se pide
		if "text" not in data: return False
		else:
			texto = data.get("text")
			if "lenguage" not in texto: return False
			if "people" not in texto: return False
			if "hashtag" not in texto: return False

		#Comrpobamos que está as horas para matar e o usuario do pc
		if "hours to kill" not in data: return False
		if "pc user" not in data: return False

		return True

			



