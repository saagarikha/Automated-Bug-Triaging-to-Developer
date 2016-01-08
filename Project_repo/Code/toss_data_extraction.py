import json
from pprint import pprint

filea=open('assigned_to.json')
dicta=json.loads(filea.read())

fileb=open('component.json')
dictb=json.loads(fileb.read())

val=""
file2 = open("toss_data","a")
pp=1
for keya,valuea in dicta.items():
	for keya1,valuea1 in valuea.items():
		#for keyb,valueb in dictb.items() :  
			#for keyb1,valueb1 in valueb.items():
		slen = len(valuea1)
		clen = len(dictb["component"][keya1])
		val=""
		flag = 0
		for i in range(0,slen,1):
			for j in range(0,clen,1):	
				if valuea1[i]["when"] == dictb["component"][keya1][j]["when"] and valuea1[i]["what"] !=None and dictb["component"][keya1][j]["what"] in ("UI","Core","Text","Debug","APT","Doc"):								
					
					if flag!=0 :
						val+=" , "
					val+=(valuea1[i]["what"])
					flag += 1
		if flag>=2:
			print(keya1)
			pp=pp+1
			val += "\n"
			print val
			file2.write(val.encode('utf-8'))
