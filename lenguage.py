import json
import os
import utilities


class Lenguage:

	def __init__(self,lenguage):

		#Lemos o arquivo
		file_path = os.path.realpath(__file__)
		path = utilities.file_to_path(file_path)
		fileName = path + "lenguage.json"
		
		#En principio non temos o idioma
		self.defecto = True

		#Se o arquivo non existe salimos do método
		if (not os.path.isfile(fileName)): return

		#Abrimos o ficheiro e lemos tóda a información
		file = open(fileName,"r")
		fileData = file.read()

		#Comrpobamos que a información e un json e cerramolo arquivo
		data = utilities.checkAndReadJson(fileData)
		file.close()
		if(not data): return

		#Se a lingua non esta, usamos a por defecto
		if lenguage not in data: return
		
		#Comrpobamos que ten tódalas claves que son necesarias
		if not self.jsonCorrecto(data.get(lenguage)): return

		self.defecto = False
		self.frases = data[lenguage]


	# Comrpobamos se o JSOn é correcto
	def jsonCorrecto(self,data):
		# Comrpobamos que estan tódolos datos do twee inicial
		if "init_tweet" not in data: return False
		else:
			init_tweet = data.get("init_tweet")
			if "part1" not in init_tweet: return False
			if "part2" not in init_tweet: return False
			if "part3" not in init_tweet: return False
			if "part4" not in init_tweet: return False
		#Comrpobamos que estan tódolos datos do tweet
		if "kill_tweet" not in data: return False
		else:
			kill_tweet = data.get("kill_tweet")
			if "week" not in kill_tweet: return False
			else:
				week_tweet = kill_tweet.get("week")
				if "first_week" not in week_tweet: return False
				if "second_week" not in week_tweet: return False
				if "third_week" not in week_tweet: return False
				if "fourth_week" not in week_tweet: return False
				if "fifth_week" not in week_tweet: return False
			if "part1" not in kill_tweet: return False
			if "month" not in kill_tweet: return False
			else:
				month_tweet = kill_tweet.get("month")
				if "1" not in month_tweet: return False
				if "2" not in month_tweet: return False
				if "3" not in month_tweet: return False
				if "4" not in month_tweet: return False
				if "5" not in month_tweet: return False
				if "6" not in month_tweet: return False
				if "7" not in month_tweet: return False
				if "8" not in month_tweet: return False
				if "9" not in month_tweet: return False
				if "10" not in month_tweet: return False
				if "11" not in month_tweet: return False
				if "12" not in month_tweet: return False
			if "part2" not in kill_tweet: return False
			if "part3" not in kill_tweet: return False
			if "part4" not in kill_tweet: return False
		if "final_tweet" not in data: return False
		else:
			final_tweet = data.get("final_tweet")
			if "part1" not in final_tweet: return False
		return True


	def fraseA1(self):
		if self.defecto: return "Esta conta enfrenta a "
		else : return self.frases.get("init_tweet").get("part1")

	def fraseA3(self):
		if self.defecto: return " cun algoritmo aleatorio que enfrentará a dúas persoas cun duelo a morte ás"
		else : return self.frases.get("init_tweet").get("part2")

	def fraseA4(self,horas):
		e = ""
		if self.defecto: e = " e "
		else: e = self.frases.get("init_tweet").get("part3")

		fraseA4 = ""
		if len(horas) == 1 :
			fraseA4 = fraseA4 + " " +str(horas[0])
		else :
			for i in range(len(horas)):
				if (i + 1) == len(horas) :
					fraseA4 = fraseA4 + e + str(horas[i])
				elif (i + 2) == len(horas) :
					fraseA4 = fraseA4 + " " + str(horas[i])
				elif i == len(horas):
					fraseA4 = fraseA4 + " " + str(horas[i])
				else :
					fraseA4 = fraseA4 + " " + str(horas[i]) + ","

		return fraseA4

	def fraseA5(self):
		if self.defecto: return " horas de cada día. Só pode quedar un! Esta é a primeira lista: "
		else : return self.frases.get("init_tweet").get("part4")

	def semanaString(self,semana):
		if self.defecto:
			if semana == 1 : return "Primeira"
			elif semana == 2 : return "Segunda"
			elif semana == 3 : return "Terceira"
			elif semana == 4 : return "Cuarta"
			else: return "Quinta"
		semanas= self.frases.get("kill_tweet").get("week")
		if semana == 1 : return semanas.get("first_week")
		elif semana == 2 : return semanas.get("second_week")
		elif semana == 3 : return semanas.get("third_week")
		elif semana == 4 : return semanas.get("fourth_week")
		else : return semanas.get("fifth_week")

	def fraseB1(self):
		if self.defecto: return " semana de "
		else : return self.frases.get("kill_tweet").get("part1")

	def monthString(self, month):
		if self.defecto:
			if month == 1: return "Xaneiro"
			elif month == 2: return "Febreiro"
			elif month == 3: return "Marzo"
			elif month == 4: return "Abril"
			elif month == 5: return "Maio"
			elif month == 6: return "Xuño"
			elif month == 7:return "Xullo"
			elif month == 8:return "Agosto"
			elif month == 9:return "Setembro"
			elif month == 10:return "Outubro"
			elif month == 11:return "Novembro"
			elif month == 12:return "Decembro"
		else:
			if month == 1: return self.frases.get("kill_tweet").get("month").get("1")
			elif month == 2: return self.frases.get("kill_tweet").get("month").get("2")
			elif month == 3: return self.frases.get("kill_tweet").get("month").get("3")
			elif month == 4: return self.frases.get("kill_tweet").get("month").get("4")
			elif month == 5: return self.frases.get("kill_tweet").get("month").get("5")
			elif month == 6: return self.frases.get("kill_tweet").get("month").get("6")
			elif month == 7:return self.frases.get("kill_tweet").get("month").get("7")
			elif month == 8:return self.frases.get("kill_tweet").get("month").get("8")
			elif month == 9:return self.frases.get("kill_tweet").get("month").get("9")
			elif month == 10:return self.frases.get("kill_tweet").get("month").get("10")
			elif month == 11:return self.frases.get("kill_tweet").get("month").get("11")
			elif month == 12:return self.frases.get("kill_tweet").get("month").get("12")


	def fraseB2(self):
		if self.defecto: return ". Ano "
		else : return self.frases.get("kill_tweet").get("part2")

	def fraseB3(self):
		if self.defecto: return " asesinou a "
		else : return self.frases.get("kill_tweet").get("part3")


	def fraseB5(self):
		if self.defecto: return " restantes. "
		else : return self.frases.get("kill_tweet").get("part4")

	def fraseC1(self):
		if self.defecto: return " é o único sobrevivente. "
		else : return self.frases.get("final_tweet").get("part1")


