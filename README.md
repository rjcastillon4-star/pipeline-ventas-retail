# Pipeline de Ventas — RetailMx

Pipeline ETL end-to-end construido en Microsoft Azure para el procesamiento y análisis de datos de ventas de una cadena minorista ficticia con 5 sucursales.

## Objetivo

Demostrar habilidades en ingeniería y análisis de datos usando servicios de Microsoft Azure, construyendo un pipeline completo desde la ingesta de datos crudos hasta la visualización en un dashboard.

## Arquitectura
## ⚙️ Servicios de Azure utilizados

| Servicio | Uso |
|---|---|
| Azure Blob Storage | Almacenamiento de archivos CSV crudos |
| Azure Data Factory | Pipeline ETL de ingesta y carga |
| Azure SQL Database | Almacén analítico de datos limpios |
| Power BI | Dashboard de visualización |

## Dataset

- 5,050 registros de ventas simuladas
- 6 meses de datos (enero a junio 2024)
- 5 sucursales: CDMX, Monterrey, Guadalajara, Puebla, Cancún
- 5 productos: Laptop, Celular, Tablet, Audífonos, Cargador
- Dataset intencionalmente imperfecto: valores nulos, duplicados y registros inválidos

## Archivos

- `part2_csv_.py` — Script Python para generar el dataset
- `querys.sql` — Queries de análisis en Azure SQL Database
- `dash1.pdf` — Dashboard exportado de Power BI

## Análisis SQL realizados

1. Ventas totales por sucursal
2. Producto más vendido por unidades
3. Tendencia de ventas mensual
4. Ticket promedio por sucursal
5. Conteo de registros con problemas de calidad de datos

## Resultados principales

- Guadalajara fue la sucursal con mayor volumen de ventas
- Celular fue el producto más vendido con más de 9,000 unidades
- Se identificaron registros con valores nulos y cantidades inválidas como parte del análisis de calidad de datos
