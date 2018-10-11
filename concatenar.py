import csv, sys, operator, pprint
import pandas as pd

print "---- Script para concatenar columnas ----"
a=0
i=0
lista = []
if(len(sys.argv)==5):
	columna1 = sys.argv[3]
	columna2 = sys.argv[4]
	ficheroin = sys.argv[1]
	ficheroout = sys.argv[2]
	with open(ficheroin, 'rbU') as f:
		#row_count = sum(1 for row in f)
		reader = csv.reader(f)
		for row in reader:
			if a<1: #estamos en la primera linea
				columna1=row.index(columna1)
				columna2=row.index(columna2)
				a=a+1
			else:
				lista.append(row[columna1]+"-"+row[columna2]) 
				if (a!=525519):
					a=a+1
	with open(ficheroin,'r') as csvinput:
		with open(ficheroout, 'w') as csvoutput:
			writer = csv.writer(csvoutput)
			for row in csv.reader(csvinput):
				i=i+1
				if i==1:
					writer.writerow(row+['tstamp'])
				else:
					writer.writerow(row+[lista[i-2]])
	print "Hecho."
else:
	print "ERROR."
	print "Uso: "
	print "concatenar.py [FICHEROIN] [FICHEROOUT] [COLUMNA1] [COLUMNA2]"
	print "	-- FICHEROIN es el fichero de entrada y del que se desea concatenar columnas. Su formato debe ser nombrefichero.csv"
	print "	-- FICHEROOUT es el fichero donde se guardara el contenido de FICHEROIN y la columna nueva producto de concatenar COLUMNA1 y COLUMNA2. Si el fichero de salida no existe lo crea y su formato debe ser nombrefichero.csv"
	
	print "	--COLUMNA1 y COLUMNA2 son las columnas que se desean concatenar."
