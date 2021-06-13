import os
from os.path import isfile, join
import pandas as pd
import csv
#import mysql.connector
import mysql.connector
ruta= r'C:/Users/hiroh/Desktop/xalo/backend/src/csv/'

contenido = os.listdir(ruta)

archivos = [nombre for nombre in contenido if isfile(join(ruta, nombre))]

datos=pd.read_csv(ruta+archivos[0],sep=';',encoding='utf-8', header=0)

df = pd.DataFrame(datos, columns=["dia","mes","año","fecha","region","id_volcan", "hr_report", "hr_evento", "tipo_evento",
     "ml", "dr","prof","tiempo_generar_reporte","comentarios", "id_nivel_alerta", "reav_y_doc"])
    

#coneccion
connection = mysql.connector.connect(host='localhost',
                                        database='xalo',
                                        user='root',
                                        password='')
cursor = connection.cursor()

for row in df.itertuples():
#ingresar datos
    cursor.execute('''
                        INSERT INTO hola (dia,mes,año,fecha,region,id_volcan, hr_report, hr_evento, tipo_evento','ml, dr,prof,tiempo_generar_reporte,comentarios, id_nivel_alerta, reav_y_doc)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        ''',
                    (row.dia,
                    row.mes,
                    row.año,
                    row.fecha,
                    row.region,
                    row.id_volcan,
                    row.hr_report,
                    row.hr_evento,
                    row.tipo_evento,
                    row.ml,
                    row.dr,
                    row.prof,
                    row.tiempo_generar_reporte,
                    row.comentarios,
                    row.id_nivel_alerta,
                    row.reav_y_doc
                    )
                )
               
    connection.commit()
