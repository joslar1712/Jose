import pandas as pd
import seaborn as sb
import gdown as gd
import matplotlib.pyplot as mp
import numpy as np
url="https://drive.google.com/uc?export=download&id=1VbrQjDF2Br0tjHHiruUnp-0qmnQwon1I"
#nombre="guion.csv"
#gd.download(url,nombre,quiet=True)
df=pd.read_csv(url)
print(df.head())
print("___________________")
df["Puntuacion de credito"]=pd.to_numeric(df["Puntuacion de credito"],errors="coerce")
df["Ingreso Mensual"]=pd.to_numeric(df["Ingreso Mensual"],errors="coerce")
#df["Region"]=pd.to_numeric(df["Region"],errors="coerce") para pasar a numerico

df["Grupo Credito"]=pd.cut(df["Puntuacion de credito"],bins=[0,300,500,600,800,900], labels=["muy malo","malo","regular","bueno","excelente"])
mp.figure(figsize=(14,6))
sb.boxplot(x="Grupo Credito",y="Ingreso Mensual",data=df,palette="Set2")
sb.swarmplot(x="Grupo Credito",y="Ingreso Mensual",data=df,color="0.25")
mp.title("hola")
mp.ylabel("eje y")
mp.xlabel("eje x")
mp.tight_layout()
mp.show()

print(df)
df.to_csv("Ejercicio clase 28-10-25.csv", index=False)