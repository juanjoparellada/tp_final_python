#FUNCIONES
def limpiar_registro_sensor(registro_raw: dict [str, str]):
    """Normaliza los valores crudos del registro de los sensores."""
    #limpiar el sensor_id
    sensor_id = registro_raw.get("sensor_id").strip()

    #Procesar temperatura
    temperatura_raw = str(registro_raw.get("temperatura", "0")).replace("°C", "").replace("C", "").strip()
    temperatura = float(temperatura_raw)

    # Ubicación
    ubicacion = registro_raw.get("ubicacion")
    if not ubicacion:
        ubicacion = "Ubicación Desconocida"
    else:
        ubicacion = ubicacion.strip()

    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

    return(registro_limpio)


def generar_resumen_sensores(lista_sensores_limpios: list[dict], umbral_temperatura: float):
    """Retorna una tupla con los IDs sobre el umbral y el promedio térmico."""
    
    if not lista_sensores_limpios:
        return([], 0.0)
    
    sensores_alerta = [
        s["sensor_id"]
        for s in lista_sensores_limpios
        if s["temperatura"] > umbral_temperatura
    ]

    total_temperatura = sum(s["temperatura"] for s in lista_sensores_limpios)
    promedio = total_temperatura / len(lista_sensores_limpios)

    return(sensores_alerta, round(promedio, 2))

#REGISTROS
registro_raw = [
    {"sensor_id": " SENSOR-001 ", 
     "temperatura": "24.5 °C", 
     "ubicacion": " Planta Norte "},
    {"sensor_id": " SENSOR-002 ", 
     "temperatura": "38.2 °C", 
     "ubicacion": "Planta Sur"},
    {"sensor_id": " SENSOR-003 ", 
     "temperatura": "26.1 °C", 
     "ubicacion": " Deposito"},
    {"sensor_id": " SENSOR-004 ", 
     "temperatura": "31.3 °C",},
    {"sensor_id": " SENSOR-005 ", 
     "temperatura": "28.4 °C", 
     "ubicacion": " Planta Oeste"},]

#Limpiar registros
datos_limpios = []

for registro in registro_raw:
    registro_limpio = limpiar_registro_sensor(registro)
    datos_limpios.append(registro_limpio)

#Análisis estadístico (umbral en 28.0 °C)
umbral = 28.0
alertas, promedio_global = generar_resumen_sensores(datos_limpios, umbral)

#Reporte final
print("=" * 45)
print("       REPORTE TÉRMICO ECOTECH")
print("=" * 45)

for i in datos_limpios:
    print(f"ID: {i['sensor_id']} | Temp: {i['temperatura']} °C | Zona: {i['ubicacion']}")
    
print("-" * 45)
print(f"Temperatura Promedio: {promedio_global} °C")
print(f"Dispositivos en Alerta (> {umbral} °C): {', '.join(alertas) if alertas else 'Ninguno'}")
print("=" * 45)