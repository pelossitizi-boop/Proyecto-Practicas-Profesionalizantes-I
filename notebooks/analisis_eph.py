
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el conjunto de datos
df = pd.read_csv("../data/eph_tecnologia_microdatos.csv")

# 2. Mostrar las primeras filas
print("PRIMEROS REGISTROS DEL DATASET")
display(df.head())

# 3. Estadísticas descriptivas
variables = ["ITF", "IX_TOT", "NIVEL_ED", "DECIFR"]

estadisticas = df[variables].agg(
    ["mean", "median", "min", "max", "std"]
).T

estadisticas.columns = [
    "Media",
    "Mediana",
    "Mínimo",
    "Máximo",
    "Desviación estándar"
]

print("ESTADÍSTICAS DESCRIPTIVAS")
display(estadisticas.round(2))

# 4. Frecuencias de las variables tecnológicas
print("TENENCIA DE COMPUTADORA")
display(df["IV12_3"].value_counts(dropna=False))

print("ACCESO A INTERNET FIJO")
display(df["II7"].value_counts(dropna=False))

# 5. Histograma de ingresos familiares
plt.figure(figsize=(8, 5))

plt.hist(
    df["ITF"].dropna(),
    bins=20,
    edgecolor="black"
)

plt.title("Distribución de los ingresos familiares")
plt.xlabel("Ingreso total familiar")
plt.ylabel("Cantidad de hogares")
plt.show()

# 6. Histograma de integrantes por hogar
plt.figure(figsize=(8, 5))

plt.hist(
    df["IX_TOT"].dropna(),
    bins=9,
    edgecolor="black"
)

plt.title("Distribución de integrantes por hogar")
plt.xlabel("Cantidad de integrantes")
plt.ylabel("Cantidad de hogares")
plt.show()
# LIMPIEZA DE DATOS

df_clean = df.copy()

variables = ["NIVEL_ED", "IV12_3", "II7"]

for columna in variables:
    df_clean[columna] = df_clean[columna].replace([-9, 9, 99], np.nan)

df_clean.to_csv("df_clean.csv", index=False)


# ANALISIS EXPLORATORIO BIVARIADO (EDA)

# Ingreso promedio según tenencia de computadora
print("INGRESO PROMEDIO SEGUN TENENCIA DE COMPUTADORA")
print(df_clean.groupby("IV12_3")["ITF"].mean())

# Computadora según decil de ingresos
print("\nCOMPUTADORA SEGUN DECIL DE INGRESOS")
print(pd.crosstab(
    df_clean["DECIFR"],
    df_clean["IV12_3"],
    normalize="index"
).round(3) * 100)

# Ingreso promedio según acceso a Internet
print("\nINGRESO PROMEDIO SEGUN ACCESO A INTERNET")
print(df_clean.groupby("II7")["ITF"].mean())

# Internet según decil de ingresos
print("\nINTERNET SEGUN DECIL DE INGRESOS")
print(pd.crosstab(
    df_clean["DECIFR"],
    df_clean["II7"],
    normalize="index"
).round(3) * 100)
