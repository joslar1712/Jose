'''🔢 Ejercicio: Boxplot y Swarmplot para Analizar la Relación entre Puntuación de Crédito e Ingreso Mensual
En este ejercicio, trabajarás con el conjunto de datos almacenado en el archivo datos_comparacion.csv. Utilizarás las bibliotecas Seaborn y Matplotlib para generar un boxplot combinado con un swarmplot, permitiendo analizar la relación entre Puntuación de Crédito e Ingreso Mensual.

📂 Fuente de datos:

🔗 Descargar archivo datos_comparacion.csv  https://drive.google.com/uc?export=download&id=1VbrQjDF2Br0tjHHiruUnp-0qmnQwon1I

El archivo de datos está disponible en datos_comparacion.csv.

Para cargar estos datos en Python, debes usar la biblioteca pandas y leer el archivo en un DataFrame.

🔹 Objetivo del ejercicio:

✅ Cargar los datos desde el archivo datos_comparacion.csv en un DataFrame de pandas.
✅ Asegurar que las columnas "Puntuación de Crédito" e "Ingreso Mensual" están correctamente definidas como valores numéricos.
✅ Utilizar Seaborn para generar un boxplot, donde:

El eje X represente la Puntuación de Crédito.
El eje Y represente el Ingreso Mensual.
✅ Superponer un swarmplot para visualizar la distribución de los datos individuales sobre el boxplot.
✅ Mostrar el gráfico para analizar la relación entre la Puntuación de Crédito y el Ingreso Mensual.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mp

#Cargando archivo csv
url="https://drive.google.com/uc?export=download&id=1VbrQjDF2Br0tjHHiruUnp-0qmnQwon1I"
df=pd.read_csv(url)
print(df.head())

#Asegurar que las columnas "Puntuación de Crédito" e "Ingreso Mensual" están definidas como valores numéricos.
#Con error coerce s encuentra el error se convierte en null
df["Puntuacion de credito"]=pd.to_numeric(df["Puntuacion de credito"],errors="coerce")
df["Ingreso Mensual"]=pd.to_numeric(df["Ingreso Mensual"],errors="coerce")
print(df.head())

df["Grupo Credito"]=pd.cut(df["Puntuacion de credito"],bins=[0,300,600,700,800,900], 
                                   labels=['Muy malo', 'Malo','regular','Bueno','Excelente'])

#Utilizar Seaborn para generar un boxplot
mp.figure(figsize=(14,6))
sns.boxplot(x="Grupo Credito", y="Ingreso Mensual", data=df, palette="Set2")

#Superponer grafico de dispersion swwarmplot
sns.swarmplot(x="Grupo Credito", y="Ingreso Mensual", data=df, color="0.25")
mp.title("Relacion entre puntuacion de credoto e ingreso mensual")
mp.xlabel("Puntuacion de Crédito")
mp.ylabel("Ingreso mensual")
mp.tight_layout()
mp.show()

