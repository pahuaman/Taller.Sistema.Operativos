# Copyright 2015 Ivxn Ortiz. Todos los derechos reservados.
import copy
import os
import time
global tamanio
class proceso:
	ide=""
	tamanio=""
	prioridad=""
	error=""
	bloque=""
	color=""
	bloqueado="10"
	estado=""
def Separar(procesazo,cadena):
	i=0
	j=0
	while(j<6):
		cacho=""
		while(cadena[i]!=":"):
			cacho=cacho+cadena[i]
			i=i+1
		if(j==0):
			procesazo.ide=cacho
		if(j==1):
			procesazo.tamanio=cacho
		if(j==2):
			procesazo.prioridad=cacho
		if(j==3):
			procesazo.error=cacho
		if(j==4):
			procesazo.bloque=cacho
		if(j==5):
			procesazo.color=cacho
		j+=1
		i+=1
def MeterALista():
	listaza.append(p1)
	listaza.append(p2)
	listaza.append(p3)
	listaza.append(p4)
def Prioridades():
	global tamanio
	temp=proceso()
	i=3
	while(i>0):
		j=0
		while(j<i):
			if(int(listaza[j].prioridad)<int(listaza[j+1].prioridad)):
				temp=listaza[j]
				listaza[j]=listaza[j+1]
				listaza[j+1]=temp
			j+=1
		i-=1
def SJF():
	global tamanio
	temp=proceso()
	i=3
	while(i>0):
		j=0
		while(j<i):
			if(int(listaza[j].tamanio)>int(listaza[j+1].tamanio)):
				temp=listaza[j]
				listaza[j]=listaza[j+1]
				listaza[j+1]=temp
			j+=1
		i-=1
def MeterNuevos():
	i=0
	while(i<4):
		nuevos.append(listaza[i])
		i+=1
def CadenaTerminados():
	i=0
	cadena=""
	totalElementos=len(terminados)
	if(totalElementos>0):
		while(totalElementos>i):
			cadena=cadena+terminados[i].ide+"-"
			i+=1
	return cadena
def CadenaNuevos():
	i=0
	cadena=""
	totalElementos=len(nuevos)
	if(totalElementos>0):
		while(totalElementos>i):
			cadena=cadena+nuevos[i].ide+"-"
			i+=1
	return cadena
def CadenaBloqueados():
	i=0
	cadena=""
	totalElementos=len(bloqueados)
	if(totalElementos>0):
		while(totalElementos>i):
			cadena=cadena+bloqueados[i].ide+"-"+str(int(bloqueados[i].bloque)-1)+"//"
			i+=1
	return cadena
def CadenaListas():
	i=0
	cadena=""
	totalElementos=len(listaza)
	if(totalElementos>0):
		while(totalElementos>i):
			cadena=cadena+listaza[i].ide+"-"
			i+=1
	return cadena
def DesenrollarCuajo(cont):
	tam=0
	i=20
	j=0
	if(len(bloqueados)>0):
		while(j<len(bloqueados)):
			if(int(bloqueados[j].bloqueado)>0):
				bloqueados[j].bloqueado=str(int(bloqueados[j].bloqueado)-1)
			else:
				listaza.append(bloqueados[0])
				bloqueados.pop(0)	
			j+=1
	if(len(ejecucion)==0):
		if(len(listaza)==0):
			print("**************************Procesadorzazo(Y)*************************")
			print("Los 5 estadazos                                 Contador:"+str(cont) )
			print("Nuevos:"+CadenaNuevos())
			print("listos: "+CadenaListas())
			print("Ejecucion: ")
			print("Bloqueados: "+CadenaBloqueados())
			print("Terminados: "+CadenaTerminados())
			time.sleep(0.5)
			os.system("cls")
			return 0
		else:
			ejecucion.append(listaza[0])
			listaza.pop(0)
			while(i>0 and int(ejecucion[0].tamanio)>0 and int(ejecucion[0].tamanio)!=int(ejecucion[0].error) and int(ejecucion[0].tamanio)!=int(ejecucion[0].bloque)):
				print("**************************Procesadorzazo(Y)*************************")
				print("Los 5 estadazos                                 Contador:"+str(cont) )
				print("Nuevos:"+CadenaNuevos())
				print("listos: "+CadenaListas())
				print("Ejecucion: "+ejecucion[0].ide+"  Tamanio: "+ejecucion[0].tamanio+"     Color: "+ejecucion[0].color)
				print("Bloqueados: "+CadenaBloqueados())
				print("Terminados: "+CadenaTerminados())
				time.sleep(0.1)
				tam=int(ejecucion[0].tamanio)
				tam-=1
				ejecucion[0].tamanio=str(tam)
				i-=1
				os.system("cls")
			if(int(ejecucion[0].tamanio)==int(ejecucion[0].error)and int(ejecucion[0].tamanio)>0):
					ejecucion[0].estado="Termino con Error"
					terminados.append(ejecucion[0])
					ejecucion.pop(0)
			else:
				if(int(ejecucion[0].tamanio)==int(ejecucion[0].bloque)and int(ejecucion[0].tamanio)>0):
					ejecucion[0].bloque=str(int(ejecucion[0].bloque)+1)
					bloqueados.append(ejecucion[0])
					ejecucion.pop(0)
				else:
					if(int(ejecucion[0].tamanio)>0):
						listaza.append(ejecucion[0])	
						ejecucion.pop(0)
					else:
						ejecucion[0].estado="OK (Y)"
						terminados.append(ejecucion[0])
						ejecucion.pop(0)
	if(len(terminados)>3):
		return 1
	return 0
#Objetazos
p1=proceso()
p2=proceso()
p3=proceso()
p4=proceso()
aux=proceso()
#listazas
listaza=[]
listaza2=[]
nuevos=[]
listos=[]
bloqueados=[]
terminados=[]
ejecucion=[]
#inciamos el programa
os.system("cls")
print ("Teclea el nombre del archivo: ")
nombreArchivo=raw_input()
nombreArchivo=nombreArchivo+".txt"
f=open(nombreArchivo,"r")
cadena=f.readline()
cadena=f.readline()
Separar(p1,cadena)
cadena=f.readline()
Separar(p2,cadena)
cadena=f.readline()
Separar(p3,cadena)
cadena=f.readline()
Separar(p4,cadena)
MeterALista()
MeterNuevos()
os.system("cls")
print("***********MENU*************")
print("*1.-FiFo                   *")
print("*2.-STF                    *")   
print("*3.-Prioridades            *")
print("****************************")
print("Tu respuesta es:")
opc=raw_input()
if(opc=="1"):
	print("ok")
if(opc=="2"):
	SJF()
if(opc=="3"):
	Prioridades()
os.system("cls")
k=0
cadena2=""
while(k<4):
	print("**************************Procesadorzazo(Y)*************************")
	print("Los 5 estadazos                                 Contador: " )
	print("Nuevos: "+CadenaNuevos())
	print("listos: "+cadena2)
	print("Ejecucion: ")
	print("Bloqueados: ")
	print("Terminados: ")
	cadena2=cadena2+listaza[k].ide+"-"
	nuevos.pop(nuevos.index(listaza[k]))
	time.sleep(0.5)
	os.system("cls")
	k+=1
band=0
cont=0
while(band==0):
	band=DesenrollarCuajo(cont)
	cont+=1
j=0
print("************Resultados**************")
print("Proceso         Estados De ejecucion")
while(j<4):
	print(terminados[j].ide+"                  "+terminados[j].estado)
	j+=1