from pymongo import MongoClient


class DB:

	def __init__(self,db_params):

		#Collemos os parametros
		url = db_params.get("url")
		port = db_params.get("port")
		dbname = db_params.get("name")
		dbuser= db_params.get("user")
		dbpassword = db_params.get("password")
		
		#Conectamonos
		uri = url + ":" + port
		connection = MongoClient(uri)
		self.bandacalowarbot = connection[dbname]
		self.bandacalowarbot.authenticate(dbuser, dbpassword)
