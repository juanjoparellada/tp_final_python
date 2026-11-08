def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4):
    """Calcula las emisiones de carbono a partir del consumo eléctrico (en KWh)."""
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros: list[dict]):
    """Procesa el historial de plantas para obtener emisiones totales y planta de mayor consumo."""

    total_global_emisiones = 0.0
    emisiones_por_planta = {}
    planta_mayor_consumo = None
    mayor_emision = -1

    for registro in registros:
        planta = registro.get("planta", "Planta Desconocida")
        consumo = registro.get("consumo_kwh", 0.0)

        emisiones = calcular_emisiones_carbono(consumo)
        total_global_emisiones += emisiones

        if planta not in emisiones_por_planta:
            emisiones_por_planta[planta] = 0.0
        else:
            emisiones_por_planta[planta] += emisiones

    for planta, emisiones in emisiones_por_planta.items():
        if emisiones > mayor_emision:
            planta_mayor_consumo = planta
            mayor_emision = emisiones

    return {
        "total_global_emisiones": round(total_global_emisiones, 2),
        "planta_mayor_consumo": planta_mayor_consumo,
        "emisiones_por_planta": emisiones_por_planta,
    }
