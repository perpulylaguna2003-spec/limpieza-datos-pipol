import pandas as pd
import numpy as np

# Cargar datos
def cargar_datos(ruta):
    return pd.read_csv(ruta)

# 1. Eliminar columnas innecesarias
def eliminar_columnas(df):
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

# 2. Manejo de valores nulos
def manejar_nulos(df):
    # Género -> moda
    df['Género'].fillna(df['Género'].mode()[0], inplace=True)
    
    # Ciudad -> "Desconocido"
    df['Ciudad'].fillna("Desconocido", inplace=True)
    
    # Nivel_Educación -> "No especificado"
    df['Nivel_Educación'].fillna("No especificado", inplace=True)
    
    return df

# 3. Corregir outliers
def corregir_outliers(df):
    # Edad (0 a 100)
    df['Edad'] = df['Edad'].apply(lambda x: x if 0 <= x <= 100 else np.nan)

    # Ingresos (>0)
    df['Ingresos'] = df['Ingresos'].apply(lambda x: x if x > 0 else np.nan)

    # Hijos (>=0)
    df['Hijos'] = df['Hijos'].apply(lambda x: x if x >= 0 else 0)

    # Altura (1.4 a 2.2)
    df['Altura'] = df['Altura'].apply(lambda x: x if 1.4 <= x <= 2.2 else np.nan)

    return df

# 4. Estandarizar texto
def limpiar_texto(df):
    df['Género'] = df['Género'].str.upper()
    df['Ciudad'] = df['Ciudad'].str.title()
    df['Nivel_Educación'] = df['Nivel_Educación'].str.title()
    return df

# 5. Pipeline completo
def limpiar_dataset(ruta):
    df = cargar_datos(ruta)
    df = eliminar_columnas(df)
    df = manejar_nulos(df)
    df = corregir_outliers(df)
    df = limpiar_texto(df)

    return df

# Ejecutar
if __name__ == "__main__":
    df_limpio = limpiar_dataset("pipol_datos.csv")
    
    print("Datos limpios:")
    print(df_limpio.head())

    df_limpio.to_csv("pipol_datos_limpio.csv", index=False)