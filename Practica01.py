# Copyright 2015 Ivxn Ortiz. Todos los derechos reservados.
import os;

def leer(archivo):
	os.system("cls")
	f=open(archivo,"r")
	faux=open("Otro.txt","w")
	faux.seek(0)
	# Empieza leer del archivo y a presentar los datos, tambien se almacenan pero ya convertidas a formato entero
	faux.write("Archivo:"+archivo+"\n")
	cadena=f.readline()
	instrucciones= int(cadena)
	faux.write("No.Instrucciones: "+ str(instrucciones)+"\n")
	cadena=f.readline()
	datos=int(cadena)
	faux.write("No. Datos: "+str(datos)+"\n")
	cadena=f.readline()
	dirinst=int(cadena)
	faux.write("Direccion inicial de instrucciones: "+str(dirinst)+"\n")
	cadena=f.readline()
	dirdatos=int(cadena)
	faux.write("Direccion inicial de datos: "+str(dirdatos)+"\n")
	i=0
	faux.write("Instrucciones:"+"\n")
	#Ciclazo while para imprimir las intrucciones del archivo
	while(i<instrucciones):
		cadena=f.readline()
		cadena=str(dirinst)+" cod: "+cadena[0]  +" dir: "+cadena[1:4]+"\n"
		dirinst+=1
		faux.write(cadena)
		i+=1
	i=0
	faux.write("Memoria:"+"\n")
	#Ciclazo while para imprimir las intrucciones del archivo
	while(i<datos):
		cadena=f.readline()
		cadena=str(dirdatos)+" valor: "+cadena+"\n"
		dirdatos+=1
		faux.write(cadena)
		i+=1
    
# Mainzazo del Programa
print("teclea el nombre de tu archivo:")
archivo=raw_input()
archivo=archivo+".txt"
# Se invoca ala funcion mostrar prar abri el archivo e imprimir su formato de la forma correspondiente
leer(archivo)