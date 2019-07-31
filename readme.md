# PythonWarBot

### WarBot para Twitter con mongo e python
Este é un WarBot para Twitter realizado en python e con persistencia de datos en MongoDB.
O xogo consiste en que os participantes vanse matando aleatoriamente entre eles ata que queda só un. A gran diferencia ca maioría de WarBots é que ademais inclúese o xeito de como se produce o asasinato e tamén de xeito aleatorio.

## Requerimentos

- Debian 9
- Python 3
- Pip
- Base de Datos en MongoDB
- Conta de developer en Twitter

## Como poñelo en funcinamento

O primeiro é modificar o arquivo **config.json** cos datos precisos:

```json
{
	"text":{
		"lenguage":"gl",
		"people":"text the name of participants",
		"hashtag":"#TextHastag"
	},
	"database":{
		"url":"",
		"port":"",
		"name":"",
		"user":"",
		"password":""
	},
	"twitter" : {
		"consumer key" :"",
		"consumer secret":"",
		"access token":"",
		"access token secret":""
	},
	"pc user":"dadmin",
	"hours to kill":[13,16,18],
	"year to start": 2020
}
``` 

Vamos comezar cos campos de *text*. En *lenguage* hai que indicar o idioma co que se publicarán os tweets. Por defecto temos *gl* que é galego e *es* que é en español. Como veremos máis adiante pódense engadir novos idiomas.O campo *people* que grupo de xente participa. Por exemplo: "famosos de Galicia". O campo *hashtag* para o hastag que se poñerá nos tweets que se publican.

En canto os campos de *database* temos que indicar a URL da base de datos, por que porto está escoitando, o nome da base de datos, un usuario da base de atos e o cantrsinal deste usuario.

Nos campos de *twitter* hai que indicar os 4 tokens que otorga unha conta de develop de twitter.

No campo *pc user* indícase o usuario do sistema co que se van executar os scripts, en *hours to kill* ten un array cas horas que queremos que se produzan as mortes e por último *year to start* para saber en que ano se iniciarán os tweets.

A continuación engádense en ***people.txt*** os participantes do xogo. Van separados por comas ou cada un nunha nova liña.

En ***ways_to_kill.txt*** temos os xeitos de matar. Cada un nunha nova liña.

A continuación executamos os seguintes comandos

```console
$ pip3 install -r requirements.txt
$ python3 main.py
```
Agora só hai que esperar a que se vaian producindo as mortes.

## Idiomas

Esta versión só conta con dous idiomas pero é doado engadir máis. Para iso hai que engadir entradas ao arquivo **lenguage.json**.

```json
{
	"es":{
		"init_tweet":{
			"part1" : "Esta cuenta enfrenta a ",
			"part2" : " con un algoritmo que enfrentará a dos personas en un duelo a muerte a las",
			"part3" : " y ",
			"part4" : " horas de cada día. Solo puede quedar uno! Esta es la primera lista: "
		},
		"kill_tweet":{
			"week": {
				"first_week": "Primera",
				"second_week": "Segunda",
				"third_week": "Tercera",
				"fourth_week": "Cuarta",
				"fifth_week": "Quinta"
			},
          "month" : {
              "1": "Enero",
              "2": "Febrero",
              "3": "Marzo",
              "4": "Abril",
              "5": "Mayo",
              "6": "Junio",
              "7": "Julio",
              "8": "Agosto",
              "9": "Septiembre",
              "10": "Octubre",
              "11": "Noviembre",
              "12": "Diciembre"
            },
			"part1" : " semana de ",
			"part2" : ". Año ",
			"part3" : " asesinó a ",
			"part4" : " restantes. "
		},
		"final_tweet": {
			"part1": " es el único superviviente. "
		}
	},
	"gl":{
		"init_tweet":{
			"part1" : "Esta conta enfrenta a ",
			"part2" : " cun algoritmo aleatorio que enfrentará a dúas persoas cun duelo a morte ás",
			"part3" : " e ",
			"part4" : " horas de cada día. Só pode quedar un! Esta é a primeira lista: "
		},
		"kill_tweet":{
			"week": {
				"first_week": "Primeira",
				"second_week": "Segunda",
				"third_week": "Terceira",
				"fourth_week": "Cuarta",
				"fifth_week": "Quinta"
			},
			"part1" : " semana de ",
            "month" : {
              "1": "Xaneiro",
              "2": "Febreiro",
              "3": "Marzo",
              "4": "Abril",
              "5": "Maio",
              "6": "Xuño",
              "7": "Xullo",
              "8": "Agosto",
              "9": "Setembro",
              "10": "Outubro",
              "11": "Novembro",
              "12": "Decembro"
            },
			"part2" : ". Ano ",
			"part3" : " asesinou a ",
			"part4" : " restantes. "
		},
		"final_tweet": {
			"part1": " é o único sobrevivente. "
		}
	}
}
```
So hai que engadir un novo campo como o de "es" ou "gl" que conteña todas as entradas para co idioma correspondente. A clave cá que se engade é a que hai que utilizar no campo *lenguage* do **config.json**.


 
