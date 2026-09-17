import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset desde CSV
df = pd.read_csv("StudentsPerformance.csv")

# Vista rápida
print(df.head())

# Estadísticas descriptivas
print(df.describe())

# Gráfico: distribución de puntajes en matemáticas
sns.histplot(df["math score"], bins=10, kde=True)
plt.title("Distribución de puntajes en Matemáticas")
plt.show()

# Relación entre lectura y escritura
sns.scatterplot(x="reading score", y="writing score", data=df)
plt.title("Relación entre lectura y escritura")
plt.show()
