# Copyright 2015 Ivxn Ortiz. Todos los derechos reservados.
import os
import time
import random 
class proceso:
	Contador="20"
def SacarDigitazos():
	dato=chr(random.randrange(48,57))
	return dato
def SacarLetraza():
	dato=chr(random.randrange(65,90))
	return dato
def IterarConBuffer(opc):
	if(opc==1):
		if(int(p1.Contador)>0 and len(bufferzazo)<21):
			bufferzazo.append(str(SacarDigitazos()))
			p1.Contador=str(int(p1.Contador)-1)		
	if(opc==2):
		if(int(p2.Contador)>0 and len(bufferzazo)<21):
			bufferzazo.append(str(SacarLetraza()))
			p2.Contador=str(int(p2.Contador)-1)	
	if(opc==3):
		if(len(bufferzazo)>0):
			bufferzazo.pop(len(bufferzazo)-1)
def ActualizaBufferzazo():
	i=0
	cadena=""
	totalElementos=len(bufferzazo)
	if(totalElementos>0):
		while(totalElementos>i):
			cadena=cadena+bufferzazo[i]
			i+=1
	return cadena
def Sorteo():
	resul=random.randrange(1,4)
	IterarConBuffer(resul)
def imprimir():
	turno=0
	while((p1.Contador!="0" and p2.Contador!="0") or len(bufferzazo)>0 ):
		Sorteo()
		print("bufferzazo: "+str(ActualizaBufferzazo()))
		print("turno: "+str(turno))
		turno+=1
		time.sleep(0.5)
		os.system("cls")
#objetazos
p1=proceso()	
p2=proceso()
p3=proceso()
bufferzazo=[]
#mainzazo(Y)
os.system("cls")
imprimir()