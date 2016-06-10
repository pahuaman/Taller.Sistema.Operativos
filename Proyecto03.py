# Copyright 2015 Ivxn Ortiz. Todos los derechos reservados.
import copy
import os
import time
acumulador=0
class proceso:
	ide=""
	tamanio=""
	prioridad=""
	error=""
	bloque=""
	bloqueado="10"
	estado=""
	def iniciar(self):
		self.DirInstrucciones=[]
		self.instrucciones=[]
	def agregarDir(self,direccion):
		self.DirInstrucciones.append(direccion)
	def agregarDat(self,datazo):
		self.instrucciones.append(datazo)

def Separar(procesazo,cadena):
	i=0
	j=0
	while(j<5):
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
		j+=1
		i+=1
def lectura():
	print ("Teclea el nombre del archivo: ")
	nombreArchivo=raw_input()
	nombreArchivo=nombreArchivo+".txt"
	#lectura de los datos del archivo
	f=open(nombreArchivo,"r")
	cadena=f.readline()#lee numero de procesos
	cadena=f.readline()#lee la cantidad de instrucciones
	NoInstruc=int(cadena[0:1])
	cadena=f.readline()#lee la cantidad de datos en memoria
	NoDatos=int(cadena[0])
	cadena=f.readline()
	Separar(p1,cadena)
	cadena=f.readline()
	Separar(p2,cadena)
	cadena=f.readline()
	Separar(p3,cadena)
	cadena=f.readline()
	Separar(p4,cadena)
	cadena=f.readline()
	Separar(p5,cadena)
	cadena=f.readline()#lee la basura ---------------
	k=0
	p1.iniciar()
	p2.iniciar()
	p3.iniciar()
	p4.iniciar()
	p5.iniciar()
	while(k<int(p1.tamanio)):
		cadena=f.readline()
		p1.agregarDir(cadena[0:3])
		p1.agregarDat(cadena[4:8])
		k+=1
	k=0
	while(k<int(p2.tamanio)):
		cadena=f.readline()
		p2.agregarDir(cadena[0:3])
		p2.agregarDat(cadena[4:8])
		k+=1
	k=0
	while(k<int(p3.tamanio)):
		cadena=f.readline()
		p3.agregarDir(cadena[0:3])
		p3.agregarDat(cadena[4:8])
		k+=1
	k=0
	while(k<int(p4.tamanio)):
		cadena=f.readline()
		p4.agregarDir(cadena[0:3])
		p4.agregarDat(cadena[4:8])
		k+=1
	k=0
	while(k<int(p5.tamanio)):
		cadena=f.readline()
		p5.agregarDir(cadena[0:3])
		p5.agregarDat(cadena[4:8])
		k+=1
	cadena=f.readline()#lee la basura --------------
	k=0
	while(k<NoDatos):
		cadena=f.readline()
		contador2.append(cadena[0:3])
		memoria.append(cadena[4:8])
		k+=1
def MeterALista():
	listaza.append(p1)
	listaza.append(p2)
	listaza.append(p3)
	listaza.append(p4)
	listaza.append(p5)
def MeterNuevos():
	i=0
	while(i<4):
		nuevos.append(listaza[i])
		i+=1
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
def gencodmaq(cadena):
	global acumulador
	if(cadena[0]=="0"):#if del salto de linea
		dif=int(cadena[1:4])-int(contador[i])
		if (dif>0):
			ac.append(str(acumulador).zfill(4))
			i+=dif
			while(dif>1):
				ac.append("0000")
				dif-=1	
		else:
			ac.append(str(acumulador).zfill(4))
	if(cadena[0]=="1"):#if donde se carga AC con la memoria
		pos=contador2.index(cadena[1:4])
		ac.append(str(int(memoria[pos])).zfill(4))
		acumulador=int(memoria[pos])
	if (cadena[0]=="2"):# if donde Escribe Ac en Memoria
		pos=contador2.index(cadena[1:4])
		memoria[pos]=str(acumulador).zfill(4)
		ac.append(str(acumulador).zfill(4))
	if (cadena[0]=="3"):#Suma AC + lo que hay en una direccion de memoria
		pos=contador2.index(cadena[1:4])
		acumulador+=int(memoria[pos])
		ac.append(str(acumulador).zfill(4))
	if (cadena[0]=="4"):#Resta AC - lo que hay en una direccion de memoria
		pos=contador2.index(cadena[1:4])
		acumulador-=int(memoria[pos])
		ac.append(str(acumulador).zfill(4))
	if (cadena[0]=="5"):#Multiplica Ac * lo que hay en una direccion de memoria
		pos=contador2.index(cadena[1:4])
		acumulador*=int(memoria[pos])
		ac.append(str(acumulador).zfill(4))
	if (cadena[0]=="6"):#Divide Ac * lo que hay en una direccion de memoria
		pos=contador2.index(cadena[1:4])
		acumulador/=int(memoria[pos].zfill(4))
		ac.append(str(acumulador).zfill(4))
	if (cadena[0]=="7"):# lee Archivo.txt y lo suma a AC
		fmem=open("Archivo.txt","r")
		aux=fmem.readline()
		if aux=="":
			aux="0000"
		acumulador+=int(aux)
		ac.append(str(acumulador).zfill(4))
	if (cadena[0]=="8"):#Escribe AC en Archivo.txt
		fmem=open("archivo.txt","w")
		fmem.seek(0)
		fmem.write(str(acumulador).zfill(4))
		ac.append(str(acumulador).zfill(4))
	if (cadena[0]=="9"):#carga el segmeneto de Datos a secundaria.txt
		j=0
		faux=open("Secundaria.txt","w")
		while(j<5):
			cadenaux=contador2[j]+"    "+memoria[j]+"\n"
			faux.write(cadenaux)
			j+=1
		faux.closed
		ac.append(str(acumulador).zfill(4))

def DesenrollarCuajo(cont):
	tam=0
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
			time.sleep(1)
			os.system("cls")
			return 0
		else:
			ejecucion.append(listaza[0])
			i=0
			listaza.pop(0)
			while(int(ejecucion[0].tamanio)>0 and int(ejecucion[0].tamanio)!=int(ejecucion[0].error) and int(ejecucion[0].tamanio)!=int(ejecucion[0].bloque)):
				print("**************************Procesadorzazo(Y)*************************")
				print("Los 5 estadazos                                 Contador:"+str(cont) )
				print("Nuevos:"+CadenaNuevos())
				print("listos: "+CadenaListas())
				print("Ejecucion: "+ejecucion[0].ide+"  Tamanio: "+ejecucion[0].tamanio)
				print("Bloqueados: "+CadenaBloqueados())
				print("Terminados: "+CadenaTerminados())
				print("Direccion instruccion: "+ejecucion[0].DirInstrucciones[0]+" Instruccion: "+ejecucion[0].instrucciones[0])
				time.sleep(1)
				tam=int(ejecucion[0].tamanio)
				tam-=1
				gencodmaq(ejecucion[0].instrucciones[0])
				dire.append(ejecucion[0].DirInstrucciones[0])
				opcode.append(ejecucion[0].instrucciones[0])
				ejecucion[0].DirInstrucciones.pop(0)
				ejecucion[0].instrucciones.pop(0)
				ejecucion[0].tamanio=str(tam)
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
	if(len(terminados)>4):
		return 1
	return 0
#Objetazos
p1=proceso()
p2=proceso()
p3=proceso()
p4=proceso()
p5=proceso()
aux=proceso()
#listazas
listaza=[]
listaza2=[]
nuevos=[]
listos=[]
bloqueados=[]
terminados=[]
ejecucion=[]
memoria=[]
contador2=[]
ac=[]
dire=[]
opcode=[]
#variables
NoInstruc=0
NoDatos=0
#inciamos el programa
os.system("cls")
lectura()#inicio de la lectura del archivo
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
	time.sleep(1)
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
while(j<5):
	print(terminados[j].ide+"                  "+terminados[j].estado)
	j+=1
j=0
tam=len(ac)
print("*************")
print("*DIR C0D3 AC*")
print("*************")
while(j<tam):
	print(" "+dire[j]+" "+opcode[j]+" "+ac[j] )
	j+=1
j=0
print("   MeMoriazo   ")
while(j<5):
	print("  "+contador2[j]+"   "+ memoria[j])
	j+=1 
