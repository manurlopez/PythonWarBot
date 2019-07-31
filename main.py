import db
import config
import datetime
from crontab import CronTab
import os
import tweepy
import calendar
from datetime import date,datetime
import utilities
import lenguage
import sys



print("Comeza a executarse o script: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

################################### Collemos a configuración do json ########################
conf = config.Config()
if conf.correctConfig == -1:
	print("Carga de configuración erronea")
	sys.exit()
print("Configuración cargada")

################################### Conectamos ca base de datos #############################
baseDeDatos = db.DB(conf.db)
warDB = baseDeDatos.bandacalowarbot
print("Conectado a base de datos")

################################## Cargamos o idioma #######################################
lingua = conf.text.get("lenguage")
leng = lenguage.Lenguage(lingua)
print("Configuración de lingua cargada")


################################### Collemos o path do script ###############################
file_path = os.path.realpath(__file__)
path = utilities.file_to_path(file_path)

###################### Creación da xente que vai a participar ###############################
# Miramos se existe a coleccion 'people'
if "people" in warDB.list_collection_names():
	# Borramos tódolos documentos da colección
	deleteQuery = {}
	warDB.people.delete_many(deleteQuery)
else:
	#Creamos a colección 'people'
	warDB.create_collection("people")

# Lemos o arquivo cos nomes da xente e creamos os documentos todos ca xente
people = []

#Abrimolo archivo con nomes da xente
fileNames = open(path + "people.txt","r")
for line in fileNames:

	#Quitamos os saltos de liña e separamos os nomes por cordas
	line = line.replace("\n","") 
	names = line.split(",")

	#Para cada nome creamos un documento que se meterá na BD
	for name in names:
		person = {"name":name, "alive":1}
		people.append(person)

#Cerramos o arquivo
fileNames.close()

#Metemos tódolos documentos na colección
warDB.people.insert_many(people)
print("Creada a colección cos participantes")

###################### Creación dos xeitos de asesinato que se poden dar ######################
# Miramos se existe a coleccion 'waystokill'
if "waystokill" in warDB.list_collection_names():
	# Borramos tódolos documentos da colección
	deleteQuery = {}
	warDB.waystokill.delete_many(deleteQuery)
else:
	#Creamos a colección 'waystokill'
	warDB.create_collection("waystokill")

# Lemos o arquivo cos nomes da xente e creamos os documentos todos ca xente
waystokill = []

#Abrimolo archivo con nomes da xente
fileWays = open(path + "waystokill.txt","r")
for line in fileWays:

	#Quitamos os saltos de liña e separamos os nomes por cordas
	line = line.replace("\n","") 
	ways = line.split(",")

	#Para cada nome creamos un documento que se meterá na BD
	for way in ways:
		wayDoc = {"text":way, "uses":0}
		waystokill.append(wayDoc)

#Cerramos o arquivo
fileWays.close()

#Metemos tódolos documentos na colección
warDB.waystokill.insert_many(waystokill)

print("Creada a colección cos xeitos de asasinar")

######################## Crear a colección para controlar o mes ##################################

# Miramos se existe a coleccion 'week'
if "week" in warDB.list_collection_names():
	# Borramos tódolos documentos da colección
	deleteQuery = {}
	warDB.week.delete_many(deleteQuery)
else:
	#Creamos a colección 'waystokill'
	warDB.create_collection("week")

day = 1
first_date = date(conf.year_start, 1, day)
while first_date.weekday() != calendar.MONDAY :
	day = day + 1
	first_date = date(int(conf.year_start), 1, day)

#Collemos o primeiro luns de xaneiro
dataInit = datetime.strptime("2020-01-06T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
document = {"date" : dataInit}
warDB.week.insert_one(document)

print("Creada a colección para controlar o tempo")

##################### Crea a imaxe #######################################################
# Creamos a imaxe
utilities.create_image(conf.image,warDB)

print("Creada a imaxe")

##################### Escribir o primeiro twett #######################################################

#Collemos as persoas que son
numberPeople = warDB.people.count_documents({})

#Collemos as frases necesarias para o texto inicial
fraseA1 = leng.fraseA1()
fraseA2 = conf.text.get("people")
fraseA3 = leng.fraseA3()
#Poñer o das horas
horas = conf.hours
fraseA4 = leng.fraseA4(horas)
fraseA5 = leng.fraseA5()
text = fraseA1 + str(numberPeople) + " " + fraseA2 + fraseA3 + fraseA4 + fraseA5

print("Creado o texto: ")
print(text)

##################### Publicamos o twet #############################################################

# Conectamos ca nosa conta
#auth = tweepy.OAuthHandler(conf.consumer_key, conf.consumer_secret)
#auth.set_access_token(conf.access_token, conf.access_token_secret)

# Collemos a API
#api = tweepy.API(auth)

#api.update_with_media("resume.png",status=text)

print("Publicado o tweet")

##################### Borramos a imaxe #############################################################
utilities.remove_image()
print("Eliminada a imaxe")

###################### Teremos que mirar para programar as horas da morte  con crontab ##############################

my_cron = CronTab(user=conf.pc_user)
killScript = "python3 " + path + 'kill.py > ' + path + 'kill.log'
job = my_cron.new(command=killScript, comment='killScript')

cronHours = ""
if len(horas) == 1 :
	cronHours = str(horas[0])
else :
	for i in range(len(horas)):
		if (i + 1) == len(horas) :
			cronHours = cronHours + str(horas[i])
		else :
			cronHours = cronHours + str(horas[i]) + ","

job.setall('0', cronHours, '*' , '*', '*')
my_cron.write()

print("Configurado o crontab")

print("Fin da aplicación")

