import db
from random import seed,randint
import calendar
from time import gmtime
from bson.objectid import ObjectId
import sys
from datetime import datetime,date,timedelta
import utilities
import tweepy
from PIL import Image, ImageDraw, ImageFont
import os
from crontab import CronTab
import config
import lenguage

print("Comeza a executarse o script: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

################################### Collemos a configuración do json ########################
conf = config.Config()
print("Configuración cargada")

################################### Conectamos ca base de datos #############################
baseDeDatos = db.DB(conf.db)
warDB = baseDeDatos.bandacalowarbot
print("Conectado a base de datos")

################################## Cargamos o idioma #######################################
lingua = conf.text.get("lenguage")
leng = lenguage.Lenguage(lingua)
print("Configuración de lingua cargada")

############################### Método que se executa no último tweet #########################
def ultimoTweet():

	#Collemos ao ganador
	winner = warDB.people.find_one(query)
	idString = str(winner.get("_id"))
	winner["_id"] = idString
	
	#Collemos o texto
	textoC1 = leng.fraseC1()
	hashtag = conf.text.get("hashtag")
	text = winner.get("name") + textoC1 + hashtag
	
	#Publicamos o twet
	#auth = tweepy.OAuthHandler(conf.consumer_key, conf.consumer_secret)
	#auth.set_access_token(conf.access_token, conf.access_token_secret)

	#Collemos a API
	#api = tweepy.API(auth)

	#api.update_status(text)

	print(text)
	
	#Deshabilitamos o crontab
	my_cron = CronTab(user=conf.pc_user)
	for job in my_cron:
		if job.comment == 'killScript' :
			my_cron.remove(job)
			my_cron.write()

	print("Deshabilitado o crontab")

################################### Collemos a semilla para ser aleatorio ###################
semilla = calendar.timegm(gmtime())

############################# Collemos ao asesino ###########################################

# Collemos o número dos que están vivos
query = { "alive" : 1 }
numberAlive = warDB.people.count_documents(query)
maxNumber = numberAlive - 1

### Se só queda un vivo avisamos
if numberAlive == 1:
	ultimoTweet()
	sys.exit()

#Collemos un número aleatorio
value = randint(0, maxNumber)

#collemos ao asesino
documents = warDB.people.find(query).limit(1).skip(value)
murder = documents[0]
idString = str(murder.get("_id"))
murder["_id"] = idString

print("Seleccionado o asasino")

############################################# Collemos a victima #############################
murderId = ObjectId(murder["_id"])
query = { "alive" : 1 , "_id": { "$ne": murderId }}
numberVictims = warDB.people.count_documents(query)
maxNumber = numberVictims - 1

#Collemos un número aleatorio
value = randint(0, maxNumber)

#Collemos a victima
documents = warDB.people.find(query).limit(1).skip(value)
victim = documents[0]
idString = str(victim.get("_id"))
victim["_id"] = idString

#Poñemos que a victima está morta
updateQuery = {"_id" : ObjectId(victim["_id"])}
warDB.people.update_one(updateQuery,{"$set" :{"alive":0}})

print("Seleccionada a víctima")

######################## Collemos o xeito de matar #########################
query = {}
numberWays = warDB.waystokill.count_documents(query)
maxNumber = numberWays - 1

#Collemos un número aleatorio
value = randint(0, maxNumber)

#Collemos a maneira de morrer
documents = warDB.waystokill.find(query).limit(1).skip(value)
way = documents[0]
idString = str(way.get("_id"))
way["_id"] = idString

print("Selecionado o xeito de matar")

######################¢¢¢¢¢¢¢¢ Collemos a data para mostrar ########################

### Collemos o número de semana e mes
week = warDB.week.find_one({})
timestamp = datetime.timestamp(week.get("date"))
dia = week.get("date").day
ano = week.get("date").year

#Collemos o primeiro luns do mes para saber que numero de semana é
month_range = calendar.monthrange(week.get("date").year, week.get("date").month)
date_corrected = date(week.get("date").year, week.get("date").month, 1)
delta = (calendar.MONDAY - month_range[0]) % 7
firstMonday = date_corrected + timedelta(days = delta)

#Calculamos os dias de diferencia co primeiro luns
diasDiferencia = dia - firstMonday.day
semanasDiferencia = diasDiferencia // 7
semana = semanasDiferencia + 1

#Aumentamos unha semana: 1000 milisegundos * 60 segundos * 60 minutos * 24 horas * 7 días
segundos = 1 * 60 * 60 * 24 * 7
newTimestamp = timestamp + segundos
newDate = datetime.fromtimestamp(newTimestamp)
warDB.week.update_one({},{"$set" :{"date":newDate}})

print("Seleccionada a data e aumentada nunha semana")

print("Creada a colección para controlar o tempo")

##################### Crea a imaxe #######################################################
# Creamos a imaxe
utilities.create_image(conf.image,warDB)

print("Creada a imaxe")

###################### Construimos o texto que se vai publicar #############

#lenguage = conf.text.get("lenguage")

semanaString = leng.semanaString(semana)
textoB1 = leng.fraseB1()
mes = leng.monthString(week.get("date").month)

#textoB2 = utilities.fraseB2(lenguage)
textoB2 = leng.fraseB2()
anoString = str(ano)

textoB3 = leng.fraseB3()

textoB4 = conf.text.get("people")
textoB5 = leng.fraseB5()
hashtag = conf.text.get("hashtag")

text = semanaString +  textoB1 + mes + textoB2 + anoString + ".\n"
text = text + murder.get("name") + textoB3 + victim.get("name") + " " + way.get("text") + ".\n"
text = text + str(numberVictims) + " " +textoB4 + textoB5 + hashtag

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
















