import json
from pprint import pprint

filea=open('assigned_to.json')
dicta=json.loads(filea.read())

fileb=open('component.json')
dictb=json.loads(fileb.read())

filec=open('short_desc.json')
dictc=json.loads(filec.read())

val=""
file2 = open("output_dev","a")
pp=1
for keya,valuea in dicta.items():
	for keya1,valuea1 in valuea.items():
		#for keyb,valueb in dictb.items() :  
			#for keyb1,valueb1 in valueb.items():
		slen = len(valuea1)
		clen = len(dictb["component"][keya1])
		blen = len(dictc["short_desc"][keya1])
		for i in range(0,slen,1):
			for j in range(0,clen,1):
				for k in range(0,blen,1) :	
					if valuea1[i]["when"] == dictb["component"][keya1][j]["when"]== dictc["short_desc"][keya1][k]["when"] and valuea1[i]["what"] !=None and dictb["component"][keya1][j]["what"] in ("UI","Core","Text","Debug","APT","Doc"):								
						print(pp)
						print(dictc["short_desc"][keya1][k]["what"] + " , "+valuea1[i]["what"] +" , "+dictb["component"][keya1][j]["what"]+"\n")
						pp=pp+1
						val=(dictc["short_desc"][keya1][k]["what"] +"  "+dictb["component"][keya1][j]["what"]+ " , "+ valuea1[i]["what"] +"\n")
						file2.write(val.encode('utf-8'))
