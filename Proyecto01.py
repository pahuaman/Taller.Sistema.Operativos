import os;
cont=0#Contador de instrucciones
cont2=0#Contador de Datos
#Fuciones de la lista
def insertarIns(dato,tipo):#esta funcion maneja como un barajeador  acomoda los datos en su lista correspondiente
	if tipo==1:
		contador.append(dato)#lista de pc de instrucciones
	if tipo==2:
		opcode.append(dato)#lista de las instrucciones
	if tipo==3:
		memoria.append(dato)#lista de los datazos
	if tipo==4:
		contador2.append(dato)#lista de pc de los datos
def Imprimir():#funcion que imprime las instrucciones y los datos, cada uno con su propio ciclo
	global cont
	print("Cuajo:\n")
	i=0			
	print("PC         IR        AC\n")#imprime el segmento de instrucciones
	while i<(len(terminado)):
		pos=contador.index(str(terminado[i]))	
		print(str(contador[pos])+"       "+str(opcode[pos])+"       "+str(ac[pos]))
		i+=1
	i=0
	print("\n")
	print("PC         MEM \n")#imprime el segmeneto de datos
	while i<cont2:
		print(str(contador2[i])+"        "+str(memoria[i]))
		i+=1	
def gencodmaq():#funcion que genera el codigo maquina
	global cont
	global cont2
	i=0
	pos=0
	acumulador=0
	while(i<cont):
		if terminado.count(str(contador[i]))==0: #valida si no esta en las listas de los ya ejecutados
			terminado.append(str(contador[i]))
			cadena=opcode[i]
			if(cadena[0]=="0"):#if del salto de linea
				dif=int(cadena[1:4])-int(contador[i])
				if dif>0:
					ac.insert(i,str(acumulador).zfill(4))
					i+=dif
					while(dif>1):
						ac.append("0000")
						dif-=1	
				else:
					ac.insert((i-(dif*-1)),str(acumulador).zfill(4))
					i+=dif
			if(cadena[0]=="1"):#if donde se carga AC con la memoria
				pos=contador2.index(cadena[1:4])
				ac.insert(i,str(int(memoria[pos])).zfill(4))
				acumulador=int(memoria[pos])
				i+=1
			if (cadena[0]=="2"):# if donde Escribe Ac en Memoria
				pos=contador2.index(cadena[1:4])
				memoria[pos]=str(acumulador).zfill(4)
				ac.insert(i,str(acumulador).zfill(4))
				i+=1
			if (cadena[0]=="3"):#Suma AC + lo que hay en una direccion de memoria
				pos=contador2.index(cadena[1:4])
				acumulador+=int(memoria[pos])
				ac.insert(i,str(acumulador).zfill(4))
				i+=1
			if (cadena[0]=="4"):#Resta AC - lo que hay en una direccion de memoria
				pos=contador2.index(cadena[1:4])
				acumulador-=int(memoria[pos])
				ac.insert(i,str(acumulador).zfill(4))
				i+=1
			if (cadena[0]=="5"):#Multiplica Ac * lo que hay en una direccion de memoria
				pos=contador2.index(cadena[1:4])
				acumulador*=int(memoria[pos])
				ac.insert(i,str(acumulador).zfill(4))
				i+=1
			if (cadena[0]=="6"):#Divide Ac * lo que hay en una direccion de memoria
				pos=contador2.index(cadena[1:4])
				acumulador/=int(memoria[pos].zfill(4))
				ac.insert(i,str(acumulador).zfill(4))
				i+=1
			if (cadena[0]=="7"):# lee Archivo.txt y lo suma a AC
				fmem=open("Archivo.txt","r")
				aux=fmem.readline()
				if aux=="":
					aux="0000"
				acumulador+=int(aux)
				ac.insert(i,str(acumulador).zfill(4))
				i+=1
			if (cadena[0]=="8"):#Escribe AC en Archivo.txt
				fmem=open("archivo.txt","w")
				fmem.seek(0)
				fmem.write(str(acumulador).zfill(4))
				ac.insert(i,str(acumulador).zfill(4))
				i+=1
			if (cadena[0]=="9"):#carga el segmeneto de Datos a secundaria.txt
				j=0
				faux=open("Secundaria.txt","w")
				while(j<cont2):
					cadenaux=contador2[j]+"    "+memoria[j]+"\n"
					faux.write(cadenaux)
					j+=1
				faux.closed
				ac.insert(i,str(acumulador).zfill(4))
				i+=1
		else:
			i+=1

def leer(archivo):#lee el archivo y lo designa a otra funcion para que sea insertado en otras listas
	global cont
	global cont2
	os.system("cls")
	f=open(archivo,"r")# Empieza leer del archivo y a presentar los datos, tambien se almacenan pero ya convertidas a formato entero
	print("Archivo:"+archivo)
	cadena=f.readline()
	instrucciones= int(cadena)
	cadena=f.readline()
	datos=int(cadena)
	cadena=f.readline()
	dirinst=int(cadena)
	cadena=f.readline()
	dirdatos=int(cadena)
	i=0
	while(i<instrucciones):#Ciclazo while para capturar el segmento de intrucciones del archivo
		a=int(f.readline())
		insertarIns(str(a).zfill(4),2)
		insertarIns(str(dirinst),1)
		cont+=1
		dirinst+=1
		i+=1
	i=0
	while(i<datos):#Ciclazo while para capturar el segmento de datos del archivo
		cadena=f.readline()
		insertarIns(cadena,3)
		insertarIns(str(dirdatos),4)
		cont2+=1
		dirdatos+=1
		i+=1
	f.closed
# Mainzazo del Programa
contador=[]
opcode=[]
ac=[]
memoria=[]
contador2=[]
terminado=[]
print("teclea el nombre de tu archivo:")
archivo=raw_input()
archivo=archivo+".txt"
leer(archivo)
gencodmaq()
Imprimir()