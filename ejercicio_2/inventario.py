import json

class StockInvalidError (Exception):
    """Excepción lanzada cuando se intenta asignar un stock negativo."""
    pass



class DispositivoEcologico():

    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

        self._stock = 0
        self.stock = stock


    @property
    def stock(self) -> int:
        return self._stock


    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise StockInvalidError(f"Error: El stock no puede ser negativo.")
        self._stock = valor

    def obtener_ficha_tecnica(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}"


class PanelSolar(DispositivoEcologico):
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int, potencia: int, eficiencia: float):
        super().__init__(codigo, nombre, precio, stock)

        self.potencia = potencia
        self.eficiencia = eficiencia

    def obtener_ficha_tecnica(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: Stock: {self.stock} | Potencia: {self.potencia} | Eficiencia Energetica: {self.eficiencia}"



class GestorInventario():

    @staticmethod
    def guardar_catalogo_json(lista_dispositivos: list[DispositivoEcologico], ruta_archivo: str):

        catalogo = []

        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.__dict__)

            if type(dispositivo) == PanelSolar:
                catalogo[-1].update({"potencia": dispositivo.potencia})
                catalogo[-1].update({"eficiencia": dispositivo.eficiencia})

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, indent=4)


#BLOQUE PRINCIPAL

catalogo = []

# Creación de productos válidos
panel1 = PanelSolar("P1", 
                    "Panel Solar 1", 
                    500, 
                    10, 
                    1000, 
                    0.8)
panel2 = PanelSolar("P2", 
                    "Panel Solar 2", 
                    600, 
                    15, 
                    1200, 
                    0.9)  
disp1 = DispositivoEcologico("P3", 
                             "Controlador de Carga 1", 
                             700, 
                             20)
disp2 = DispositivoEcologico("P4", 
                             "Entrada de Energia 1", 
                             800, 
                             25)

catalogo.extend([panel1, panel2, disp1, disp2])

# Demostración del polimorfismo
print("--- Fichas Técnicas ---")
for prod in catalogo:
    print(prod.obtener_ficha_tecnica())
    print("-" * 30)

# Captura controlada de StockInvalidError
print("\n--- Validación de Excepción ---")
try:
    print("Intentando asignar stock negativo a un producto...")
    disp_error = DispositivoEcologico("P5", 
                                  "Entrada de Energía 2", 
                                  900, 
                                  -1)
except StockInvalidError as error:
    print(f"Error controlado: {error}") 

# Guardar catalogo en JSON
admin_catalogo = GestorInventario()
admin_catalogo.guardar_catalogo_json(catalogo, "catalogo_ecotech.json")
print(f"Catálogo guardado exitosamente.")
