# Tracker de Inversiones

> Script en Python para analizar un portafolio de inversiones desde un archivo JSON.

---

## 🇲🇽 Español

### Descripción
Script desarrollado en Python que lee un portafolio de inversiones en formato JSON y calcula el total invertido por semana y por broker. Usa `Decimal` para evitar errores de redondeo en cálculos financieros. Compatible con múltiples brokers (GBM y Bitso).

### Tecnologías
- Python 3
- Módulo `json`
- Módulo `decimal`

### Características
- Lee inversiones organizadas por semana desde un JSON
- Calcula el total invertido por semana
- Calcula el total por broker
- Calcula el total general invertido
- Usa precisión decimal para evitar errores de redondeo en cálculos financieros

### Instalación

**Requisitos:**
- Python 3

**Pasos:**
```bash
# 1. Clonar el repositorio
git clone https://github.com/Chiripi0rca/tracker-inversiones.git
cd tracker-inversiones

# 2. Copiar el archivo de ejemplo y renombrarlo
cp portafolio.example.json portafolio.json

# 3. Editar portafolio.json con tus datos reales

# 4. Correr el script
python main.py
```

### Estructura del JSON
```json
{
  "accounts": {
    "GBM": {
      "currency": "MXN",
      "holdings": [
        {"notes": "primera inversion 01/01/2026"},
        {"ticker": "FUNO11", "type": "FIBRA", "shares": 10, "avg_cost": 25.00}
      ]
    },
    "Bitso": {
      "currency": "MXN",
      "holdings": [
        {"notes": "primera inversion 02/01/2026"},
        {"ticker": "VTI", "type": "ETF", "shares": 0.05, "avg_cost": 6000.00}
      ]
    }
  }
}
```

### Ejemplo de salida
```
primera inversion 01/01/2026
FUNO11: 10 * 25.0 = 250.00
______________________________

El total de la primera inversion del 01/01/2026 fue: 250.00
______________________________

_________________________________

Total invertido en GBM es : 250.00
_________________________________

Total invertido es: 250.00
```

### Autor
Ricardo — [GitHub](https://github.com/Chiripi0rca)

---

## 🇺🇸 English

### Description
Python script that reads an investment portfolio from a JSON file and calculates the total invested per week and per broker. Uses `Decimal` to avoid floating-point rounding errors in financial calculations. Compatible with multiple brokers (GBM and Bitso).

### Tech Stack
- Python 3
- `json` module
- `decimal` module

### Features
- Reads weekly investments from a JSON file
- Calculates total invested per week
- Calculates total per broker
- Calculates overall total invested
- Uses decimal precision to avoid rounding errors in financial calculations

### Setup

**Requirements:**
- Python 3

**Steps:**
```bash
# 1. Clone the repository
git clone https://github.com/Chiripi0rca/tracker-inversiones.git
cd tracker-inversiones

# 2. Copy the example file and rename it
cp portafolio.example.json portafolio.json

# 3. Edit portafolio.json with your real data

# 4. Run the script
python main.py
```

### Author
Ricardo Ramos Puga — [GitHub](https://github.com/Chiripi0rca)
