class ManejadorSoporte:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def manejarSolicitud(self, nivel):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class SoporteNivel1(ManejadorSoporte):
    def manejarSolicitud(self, nivel):
        if nivel == 1:
            print("Soporte Nivel 1: Problema resuelto.")
        elif self.siguiente:
            print("Soporte Nivel 1: Escalando al siguiente nivel...")
            self.siguiente.manejarSolicitud(nivel)
        else:
            print("Soporte Nivel 1: No hay más niveles disponibles.")

class SoporteNivel2(ManejadorSoporte):
    def manejarSolicitud(self, nivel):
        if nivel == 2:
            print("Soporte Nivel 2: Problema resuelto.")
        else:
            print("Soporte Nivel 2: No se puede resolver este problema. Contactar con un administrador.")

class Cliente:
    def __init__(self):
        # Crea la cadena: Nivel1 → Nivel2
        self.cadena = SoporteNivel1(
            SoporteNivel2()
        )

    def realizarSolicitud(self, nivel):
        print(f"\nCliente: Solicitud de soporte para nivel {nivel}")
        self.cadena.manejarSolicitud(nivel)

cliente = Cliente()
cliente.realizarSolicitud(1)  # Soporte Nivel 1
cliente.realizarSolicitud(2)  # Soporte Nivel 2
cliente.realizarSolicitud(3)  # No puede resolverse
