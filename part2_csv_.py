import pandas as pd
import numpy as np
import random
from datetime import date, timedelta

sucursales = ["Lima", "Arequipa", "Trujillo", "Cusco", "Piura"]
productos = ["Laptop", "Celular", "Tablet", "Audifonos", "Cargador"]

filas = []

for _ in range(5000):
    fecha = date(2024,1,1) + timedelta(days=random.randint(0,180))
    
    #nulls en sucursal
    sucursal = random.choice(sucursales) if random.random() > 0.03 else None
    
    #nulls en producto
    producto = random.choice(productos) if random.random() > 0.04 else None
    
    #nulls en cantidad y algun valor invalido
    if random.random() > 0.02:
        cantidad = random.randint(0,20) if random.random()>0.01 else -1
    else:
        cantidad = None
    
    #nulls en precio y algun valor invalido
    if random.random():
        precio = random.choice([299, 350, 600, 1500, 4000, 687]) if random.random()>0.02 else 0
    else:
        precio = None
    
    #total venta
    if precio is not None and cantidad is not None:
        total = precio * cantidad
    else: total = None
    
    filas.append({
        "fecha": fecha,
        "sucursal": sucursal,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "total_venta": total
        })
        
df = pd.DataFrame(filas)
duplicados = df.sample(frac = 0.01)
df = pd.concat([df, duplicados]).sample(frac=1).reset_index(drop = True)

df.to_csv("ventas_p2_real.csv", index = False)
print(len(df))
print(df.isnull().sum())

        
        
        
        


