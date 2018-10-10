# concatenar_columnas_csv

Script de Python que permite concatenar dos columnas de un mismo fichero formato CSV.

```
"concatenar.py [FICHEROIN] [FICHEROOUT] [COLUMNA1] [COLUMNA2]"
	print "	-- FICHEROIN es el fichero de entrada y del que se desea concatenar columnas. Su formato debe ser nombrefichero.csv"
	print "	-- FICHEROOUT es el fichero donde se guardara el contenido de FICHEROIN y la columna nueva producto de concatenar COLUMNA1 y COLUMNA2. Si el fichero de salida no existe lo crea y su formato debe ser nombrefichero.csv"
	
	print "	--COLUMNA1 y COLUMNA2 son las columnas que se desean concatenar."
```
El siguiente ejemplo trata de concatenar las columnas Dia y Hora del fichero data.csv y genera un nuevo fichero denominado dataout.csv que puede estar creado o se crea de manera automática.

```
python concatenar.py data.csv dataout.csv Dia Hora
```
