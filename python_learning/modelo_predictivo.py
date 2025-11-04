import pandas as pd
from sklearn.linear_model import LinearRegression

# Datos históricos
df = pd.DataFrame({
    'horas_estudio': [1, 2, 3, 4, 5],
    'nota': [50, 60, 65, 70, 80]
})


# Entrenamiento del modelo
modelo = LinearRegression()
modelo.fit(df[['horas_estudio']], df['nota'])

# Predicción
print(modelo.predict([[6]]))  # Qué nota tendría si estudia 6 horas
