
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el conjunto de datos
df = pd.read_csv("eph_tecnologia_microdatos.csv")

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
